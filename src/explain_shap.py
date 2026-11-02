"""
Explainable AI (TreeSHAP) Pipeline for Automobile Insurance Fraud Detection
Reproducing Fig. 3, Fig. 4, and Fig. 5 of Ding et al. (2025)
"""

import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lightgbm as lgb
import shap

TEST_PATH = os.path.join("data", "processed", "test.csv")
TRAIN_PATH = os.path.join("data", "processed", "train.csv")
MODELS_DIR = os.path.join("src", "models")
BEST_MODEL_PATH = os.path.join(MODELS_DIR, "best_lightgbm.joblib")
FIGURES_DIR = os.path.join("research", "figures")

def run_shap_analysis():
    os.makedirs(FIGURES_DIR, exist_ok=True)
    print(f"[*] Loading test data: {TEST_PATH}")
    test_df = pd.read_csv(TEST_PATH)
    
    target_col = "FraudFound_P"
    X_test = test_df.drop(columns=[target_col])
    y_test = test_df[target_col].astype(int)

    # Load model
    if os.path.exists(BEST_MODEL_PATH):
        print(f"[*] Loading model from: {BEST_MODEL_PATH}")
        model = joblib.load(BEST_MODEL_PATH)
    else:
        print("[!] Pre-trained model not found. Training a balanced LightGBM model...")
        train_df = pd.read_csv(TRAIN_PATH)
        X_train = train_df.drop(columns=[target_col])
        y_train = train_df[target_col].astype(int)
        model = lgb.LGBMClassifier(scale_pos_weight=16.0, random_state=42, verbose=-1)
        model.fit(X_train, y_train)

    print("[*] Calculating TreeSHAP values...")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(X_test)

    # 1. Figure 3: Ranking of SHAP values (mean absolute)
    print("[*] Generating Figure 3: Mean absolute SHAP value ranking...")
    plt.figure(figsize=(10, 8), dpi=300)
    shap.plots.bar(shap_values, max_display=15, show=False)
    plt.title("Ranking of SHAP Values (Mean Absolute) for Insurance Fraud Prediction", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    fig3_path = os.path.join(FIGURES_DIR, "fig3_shap_ranking.png")
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"    Saved Figure 3 to: {fig3_path}")

    # 2. Figure 4: Summary Plot (Bee-swarm)
    print("[*] Generating Figure 4: SHAP summary plot (bee-swarm)...")
    plt.figure(figsize=(10, 8), dpi=300)
    shap.plots.beeswarm(shap_values, max_display=15, show=False)
    plt.title("Summary Plot of SHAP Values Across Test Samples", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    fig4_path = os.path.join(FIGURES_DIR, "fig4_shap_summary.png")
    plt.savefig(fig4_path, dpi=300)
    plt.close()
    print(f"    Saved Figure 4 to: {fig4_path}")

    # 3. Figure 5: Dependence Plot (Interaction between top features)
    print("[*] Generating Figure 5: SHAP dependence interaction plot...")
    plt.figure(figsize=(9, 6), dpi=300)
    # Check top feature and interact with VehicleCategory or VehiclePrice
    top_feature = X_test.columns[np.argmax(np.abs(shap_values.values).mean(axis=0))]
    interact_feature = "VehicleCategory" if "VehicleCategory" in X_test.columns else None
    
    shap.plots.scatter(shap_values[:, top_feature], color=shap_values[:, interact_feature] if interact_feature else None, show=False)
    plt.title(f"SHAP Dependence Plot: {top_feature} vs {interact_feature}", fontsize=12, fontweight='bold', pad=15)
    plt.tight_layout()
    fig5_path = os.path.join(FIGURES_DIR, "fig5_shap_dependency.png")
    plt.savefig(fig5_path, dpi=300)
    plt.close()
    print(f"    Saved Figure 5 to: {fig5_path}")

    print("[+] All TreeSHAP figures successfully generated and saved to research/figures/")

if __name__ == "__main__":
    run_shap_analysis()
