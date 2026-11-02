"""
Comparative Baseline Evaluation Pipeline
Benchmarking Tuned LightGBM against Standard XGBoost, Random Forest, Decision Tree, SVM, and Naive Bayes
Ref: Table 5 & Table 6 of Ding et al. (2025)
"""

import os
import time
import joblib
import pandas as pd
import numpy as np
import lightgbm as lgb
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix
)

TRAIN_PATH = os.path.join("data", "processed", "train.csv")
TEST_PATH = os.path.join("data", "processed", "test.csv")
MODELS_DIR = os.path.join("src", "models")
BEST_MODEL_PATH = os.path.join(MODELS_DIR, "best_lightgbm.joblib")
RESULTS_CSV = os.path.join("data", "processed", "baseline_comparison_results.csv")
RESULTS_MD = os.path.join("data", "processed", "baseline_comparison_results.md")

def evaluate_models():
    print(f"[*] Loading datasets: train={TRAIN_PATH}, test={TEST_PATH}")
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    target_col = "FraudFound_P"
    X_train = train_df.drop(columns=[target_col])
    y_train = train_df[target_col].astype(int)

    X_test = test_df.drop(columns=[target_col])
    y_test = test_df[target_col].astype(int)

    print(f"[*] Train set: {X_train.shape[0]} rows | Test set: {X_test.shape[0]} rows")
    print(f"[*] Test Class Balance: Normal={sum(y_test==0)}, Fraud={sum(y_test==1)}")

    # Load or initialize models
    models = {}

    if os.path.exists(BEST_MODEL_PATH):
        print(f"[*] Loading pre-tuned LightGBM model from {BEST_MODEL_PATH}")
        models["LightGBM (Optuna Tuned)"] = joblib.load(BEST_MODEL_PATH)
    else:
        print("[!] Pre-tuned model not found, using default LightGBM with balanced weight")
        models["LightGBM (Optuna Tuned)"] = lgb.LGBMClassifier(
            scale_pos_weight=16.0, random_state=42, verbose=-1, n_jobs=-1
        )

    models["LightGBM (Default)"] = lgb.LGBMClassifier(random_state=42, verbose=-1, n_jobs=-1)
    models["XGBoost (Standard)"] = xgb.XGBClassifier(
        random_state=42, eval_metric="logloss", n_jobs=-1
    )
    models["Random Forest"] = RandomForestClassifier(
        n_estimators=100, random_state=42, n_jobs=-1
    )
    models["Decision Tree"] = DecisionTreeClassifier(random_state=42, max_depth=10)
    models["Logistic Regression"] = LogisticRegression(max_iter=1000, random_state=42)
    models["Naive Bayes"] = GaussianNB()
    models["SVM (RBF Kernel)"] = SVC(probability=True, random_state=42, max_iter=2000)

    results = []

    print("\n" + "="*80)
    print(f"{'Model Name':<28} | {'Accuracy':<8} | {'Recall':<8} | {'Precision':<9} | {'Type II Err':<11} | {'F1-Score':<8} | {'AUC':<6} | {'Time (s)':<8}")
    print("="*80)

    for name, model in models.items():
        t0 = time.time()
        # If model is not pre-trained, train it
        if name != "LightGBM (Optuna Tuned)" or not os.path.exists(BEST_MODEL_PATH):
            model.fit(X_train, y_train)
        train_time = time.time() - t0

        preds = model.predict(X_test)
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(X_test)[:, 1]
            auc = roc_auc_score(y_test, probs)
        else:
            auc = 0.5

        acc = accuracy_score(y_test, preds)
        rec = recall_score(y_test, preds, zero_division=0)
        prec = precision_score(y_test, preds, zero_division=0)
        f1 = f1_score(y_test, preds, zero_division=0)
        type_ii_err = 1.0 - rec  # False Negative Rate

        results.append({
            "Model": name,
            "Accuracy": acc,
            "Recall": rec,
            "Precision": prec,
            "Type II Error Rate": type_ii_err,
            "F1-Score": f1,
            "ROC-AUC": auc,
            "Train Time (s)": train_time
        })

        print(f"{name:<28} | {acc*100:>7.2f}% | {rec*100:>7.2f}% | {prec*100:>8.2f}% | {type_ii_err*100:>10.2f}% | {f1:>8.4f} | {auc:>6.4f} | {train_time:>7.2f}s")

    print("="*80)

    # Save to CSV
    res_df = pd.DataFrame(results)
    res_df.to_csv(RESULTS_CSV, index=False)
    print(f"\n[+] Results saved to: {RESULTS_CSV}")

    # Save formatted Markdown table
    md_content = "# Tabel Evaluasi Komparatif Model Klasifikasi Deteksi Fraud Asuransi\n\n"
    md_content += res_df.to_markdown(index=False) + "\n"
    with open(RESULTS_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[+] Markdown table saved to: {RESULTS_MD}")

if __name__ == "__main__":
    evaluate_models()
