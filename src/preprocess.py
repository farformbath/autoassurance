"""
Data Preprocessing Pipeline for Automobile Insurance Fraud Detection
Dataset: Vehicle Insurance Claim Fraud Detection (fraud_oracle.csv)
Ref: Ding et al. (2025), Insurance Mathematics and Economics
"""

import os
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

RAW_PATH = os.path.join("data", "raw", "fraud_oracle.csv")
PROCESSED_DIR = os.path.join("data", "processed")
META_PATH = os.path.join(PROCESSED_DIR, "preprocessing_meta.json")

def clean_and_preprocess(raw_path=RAW_PATH, processed_dir=PROCESSED_DIR):
    os.makedirs(processed_dir, exist_ok=True)
    print(f"[1/5] Loading raw dataset from: {raw_path}")
    df = pd.read_csv(raw_path)
    print(f"      Initial shape: {df.shape[0]} rows, {df.shape[1]} columns")

    # 1. Clean bad data / invalid entries
    print("[2/5] Cleaning bad data and anomaly entries...")
    # Drop corrupted claim date rows
    invalid_dates = (df['DayOfWeekClaimed'] == '0') | (df['MonthClaimed'] == '0')
    df = df[~invalid_dates].copy()
    
    # Handle Age == 0 anomaly
    # If Age is 0, replace with median age of that PolicyHolder age group
    zero_age = df['Age'] == 0
    if zero_age.sum() > 0:
        median_age = df[df['Age'] > 0]['Age'].median()
        df.loc[zero_age, 'Age'] = median_age
        print(f"      Imputed {zero_age.sum()} records with Age=0 using median Age={median_age:.1f}")

    print(f"      Rows after initial cleaning: {df.shape[0]}")

    # 2. Separate Target and Feature Columns
    target_col = "FraudFound_P"
    id_cols = ["PolicyNumber"]
    
    y = df[target_col].astype(int)
    X = df.drop(columns=[target_col] + id_cols)

    # 3. Categorical Encoding
    print("[3/5] Encoding categorical and ordinal variables...")
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    label_encoders = {}
    for col in cat_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        label_encoders[col] = {str(k): int(v) for k, v in zip(le.classes_, range(len(le.classes_)))}

    # 4. Stratified Split 80:20 (80% Train, 20% Test)
    print("[4/5] Performing Stratified 80:20 Train-Test Split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # 5. Z-Score Normalization (StandardScaler)
    print("[5/5] Applying Z-Score Normalization...")
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns, index=X_train.index)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X.columns, index=X_test.index)

    # Save processed datasets
    train_df = X_train_scaled.copy()
    train_df[target_col] = y_train.values
    
    test_df = X_test_scaled.copy()
    test_df[target_col] = y_test.values

    train_out = os.path.join(processed_dir, "train.csv")
    test_out = os.path.join(processed_dir, "test.csv")
    
    train_df.to_csv(train_out, index=False)
    test_df.to_csv(test_out, index=False)
    print(f"      Saved train dataset: {train_out} ({train_df.shape})")
    print(f"      Saved test dataset:  {test_out} ({test_df.shape})")

    # Save metadata
    meta = {
        "raw_rows": int(len(df)),
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "num_features": int(X.shape[1]),
        "feature_names": list(X.columns),
        "target_distribution": {
            "train": {str(k): int(v) for k, v in y_train.value_counts().items()},
            "test": {str(k): int(v) for k, v in y_test.value_counts().items()},
            "imbalance_ratio": f"1:{int(y.value_counts()[0] / y.value_counts()[1])}"
        },
        "scaler_mean": {col: float(m) for col, m in zip(X.columns, scaler.mean_)},
        "scaler_scale": {col: float(s) for col, s in zip(X.columns, scaler.scale_)}
    }

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print(f"      Saved preprocessing metadata: {META_PATH}")
    print("Preprocessing completed successfully!")

if __name__ == "__main__":
    clean_and_preprocess()
