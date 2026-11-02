---
name: ml-modeling-agent
description: Specialized machine learning agent for end-to-end data preprocessing, Optuna Bayesian hyperparameter tuning, cross-validation, baseline benchmarking, and TreeSHAP explainability for automobile insurance fraud detection.
---

# Skill: ML Modeling Agent (Machine Learning & Modeling Automation)

Skill ini digunakan untuk mengeksekusi pipeline machine learning lengkap, mulai dari pembersihan dataset mentah `data/raw/fraud_oracle.csv`, penanganan class imbalance (1:16), optimasi hyperparameter **LightGBM** via **Optuna (TPE)**, pengujian komparatif model baseline, hingga ekstraksi interpretabilitas **TreeSHAP**.

---

## 🎯 Tanggung Jawab & Kontrak Agen

1. **Zero Data Fabrication (Integritas Mutlak)**:
   * Seluruh angka metrik (Akurasi, Presisi, Recall, F1, Type II error, AUC) WAJIB bersumber dari eksekusi nyata skrip Python pada dataset acuan.
   * DILARANG mengarang angka performa di dokumen naskah sebelum skrip dieksekusi.
2. **Kesesuaian dengan Paper Acuan (Ding et al., 2025)**:
   * Menggunakan variabel target biner `FraudFound_P` (1 = fraud, 0 = normal).
   * Menerapkan pembagian 80% Training Set dan 20% Test Set secara *Stratified Sampling*.
   * Menggunakan 5-Fold Stratified Cross-Validation selama tuning.
   * Menyajikan tabel perbandingan performa yang setara dengan Tabel 5 & Tabel 6 pada paper acuan.

---

## 📁 Struktur File & Alur Kerja di `src/`

```
src/
├── preprocess.py        # Tahap 1: Data cleaning, encoding, Z-score, resampling, split 80:20
├── tune_optuna.py       # Tahap 2: Bayesian hyperparameter tuning LightGBM via Optuna (TPE)
├── evaluate.py          # Tahap 3: Benchmarking komparatif vs baseline (XGBoost, RF, DT, SVM, NB)
└── explain_shap.py      # Tahap 4: Analisis XAI TreeSHAP (Feature ranking, Summary & Dependency plot)
```

---

## 🚀 Perintah Eksekusi CLI

### 1. Eksekusi Pra-Pemrosesan Data
```bash
python src/preprocess.py
```
* **Input**: `data/raw/fraud_oracle.csv`
* **Output**:
  * `data/processed/train.parquet` (atau `.csv`)
  * `data/processed/test.parquet`
  * `data/processed/preprocessing_meta.json` (statistik fitur, daftar kolom encoding, mean & std)

### 2. Eksekusi Tuning Hyperparameter Optuna
```bash
python src/tune_optuna.py --trials 100 --seed 42
```
* **Metode**: Optuna `TPESampler` + `MedianPruner` dengan 5-Fold Stratified CV.
* **Fungsi Objektif**: Memaksimalkan F1-Score atau meminimalkan Type II Error Rate ($1 - \text{Recall}$).
* **Output**:
  * `data/processed/best_hyperparameters.json`
  * `data/processed/optuna_study_summary.csv`
  * Model tersimpan di `src/models/best_lightgbm.joblib`

### 3. Eksekusi Evaluasi Komparatif Baseline
```bash
python src/evaluate.py
```
* **Model yang Diuji**:
  1. LightGBM (Optuna Tuned)
  2. LightGBM (Default)
  3. XGBoost (Standard Baseline Ding et al.)
  4. Random Forest
  5. Decision Tree
  6. Support Vector Machine (SVM)
  7. Naive Bayes
* **Output**:
  * `data/processed/baseline_comparison_results.csv`
  * Ringkasan Markdown untuk tabel Bab 4 / naskah proposal skripsi.

### 4. Eksekusi Interpretabilitas TreeSHAP & Visualisasi
```bash
python src/explain_shap.py
```
* **Output Gambar Publikasi**:
  * `research/figures/fig3_shap_ranking.png` (Ranking nilai absolut rata-rata SHAP)
  * `research/figures/fig4_shap_summary.png` (Summary bee-swarm plot seluruh sampel)
  * `research/figures/fig5_shap_dependency.png` (Dependency plot interaksi fitur)
  * `research/figures/confusion_matrix_comparison.png`
  * `research/figures/roc_pr_curves.png`

---

## ✅ Kriteria Verifikasi Hasil
- [ ] File dataset bersih tersimpan di `data/processed/` dengan integritas baris terverifikasi.
- [ ] Laporan evaluasi memuat metrik: Accuracy, Recall, Precision, Type II Error Rate, F1-Score, dan ROC-AUC.
- [ ] Seluruh grafik tersimpan di `research/figures/` dalam resolusi tinggi (DPI $\ge 300$).
