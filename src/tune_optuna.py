"""
Hyperparameter Optimization of LightGBM using Optuna (TPE)
Cross-Validation: Stratified 5-Fold
Objective: Maximize F1-Score and Minimize Type II Error Rate
"""

import os
import json
import argparse
import joblib
import pandas as pd
import numpy as np
import lightgbm as lgb
import optuna
from optuna.samplers import TPESampler
from optuna.pruners import MedianPruner
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, recall_score, precision_score

# Suppress Optuna verbose logs by default
optuna.logging.set_verbosity(optuna.logging.WARNING)

TRAIN_PATH = os.path.join("data", "processed", "train.csv")
MODELS_DIR = os.path.join("src", "models")
BEST_PARAMS_PATH = os.path.join("data", "processed", "best_hyperparameters.json")
STUDY_SUMMARY_PATH = os.path.join("data", "processed", "optuna_study_summary.csv")

def run_optuna_tuning(n_trials=50, seed=42):
    os.makedirs(MODELS_DIR, exist_ok=True)
    print(f"[*] Loading training data from: {TRAIN_PATH}")
    train_df = pd.read_csv(TRAIN_PATH)
    
    target_col = "FraudFound_P"
    X = train_df.drop(columns=[target_col])
    y = train_df[target_col].astype(int)
    
    print(f"[*] Training features: {X.shape[1]}, Records: {X.shape[0]} (Fraud={sum(y==1)}, Normal={sum(y==0)})")
    print(f"[*] Initializing Optuna study with TPE Sampler ({n_trials} trials, seed={seed})...")

    def objective(trial):
        params = {
            'objective': 'binary',
            'metric': 'binary_logloss',
            'boosting_type': 'gbdt',
            'random_state': seed,
            'verbose': -1,
            'n_jobs': -1,
            'num_leaves': trial.suggest_int('num_leaves', 15, 255),
            'max_depth': trial.suggest_int('max_depth', 3, 12),
            'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
            'n_estimators': trial.suggest_int('n_estimators', 50, 400),
            'min_child_samples': trial.suggest_int('min_child_samples', 10, 80),
            'subsample': trial.suggest_float('subsample', 0.5, 1.0),
            'subsample_freq': 1,
            'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
            'reg_alpha': trial.suggest_float('reg_alpha', 1e-8, 10.0, log=True),
            'reg_lambda': trial.suggest_float('reg_lambda', 1e-8, 10.0, log=True),
            'scale_pos_weight': trial.suggest_float('scale_pos_weight', 1.0, 16.0)
        }

        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
        fold_f1_scores = []
        fold_recalls = []

        for fold, (train_idx, val_idx) in enumerate(cv.split(X, y)):
            X_tr, y_tr = X.iloc[train_idx], y.iloc[train_idx]
            X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]

            model = lgb.LGBMClassifier(**params)
            model.fit(X_tr, y_tr)

            preds = model.predict(X_val)
            f1 = f1_score(y_val, preds, zero_division=0)
            rec = recall_score(y_val, preds, zero_division=0)

            fold_f1_scores.append(f1)
            fold_recalls.append(rec)

        mean_f1 = np.mean(fold_f1_scores)
        mean_rec = np.mean(fold_recalls)
        # Composite score prioritizing F1 with high recall (low Type II error)
        score = 0.7 * mean_f1 + 0.3 * mean_rec
        return score

    sampler = TPESampler(seed=seed)
    pruner = MedianPruner(n_startup_trials=5, n_warmup_steps=10)
    study = optuna.create_study(direction="maximize", sampler=sampler, pruner=pruner)

    study.optimize(objective, n_trials=n_trials, show_progress_bar=True)

    print(f"\n[+] Optimization finished!")
    print(f"    Best Trial Value: {study.best_value:.4f}")
    print("    Best Hyperparameters:")
    for k, v in study.best_params.items():
        print(f"      - {k}: {v}")

    # Save best parameters
    with open(BEST_PARAMS_PATH, "w", encoding="utf-8") as f:
        json.dump(study.best_params, f, indent=2)
    print(f"    Saved best parameters to: {BEST_PARAMS_PATH}")

    # Save study summary
    trials_df = study.trials_dataframe()
    trials_df.to_csv(STUDY_SUMMARY_PATH, index=False)
    print(f"    Saved study trials summary to: {STUDY_SUMMARY_PATH}")

    # Retrain final model on full train dataset
    print("[*] Retraining final LightGBM model on full training set...")
    final_params = study.best_params.copy()
    final_params.update({
        'objective': 'binary',
        'metric': 'binary_logloss',
        'boosting_type': 'gbdt',
        'random_state': seed,
        'verbose': -1,
        'n_jobs': -1
    })

    final_model = lgb.LGBMClassifier(**final_params)
    final_model.fit(X, y)

    model_path = os.path.join(MODELS_DIR, "best_lightgbm.joblib")
    joblib.dump(final_model, model_path)
    print(f"[+] Final trained model saved to: {model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=30, help="Number of Optuna trials")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()
    run_optuna_tuning(n_trials=args.trials, seed=args.seed)
