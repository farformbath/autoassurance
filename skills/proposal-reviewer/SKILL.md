---
name: proposal-reviewer
description: Panduan tahap akhir (End) untuk audit kualitas, validasi struktur naskah Bab 1, 2, dan 3, serta verifikasi kepatuhan terhadap Template Resmi Proposal Skripsi UNNES 2026 dan 11 poin revisi Bimbingan 1.
---

# Skill: Proposal Reviewer (Tahap 4: Review & Audit Kualitas Naskah)

Skill ini digunakan pada **Tahap Akhir (End)** sebelum naskah proposal skripsi diajukan ke dosen pembimbing atau seminar proposal. Fokusnya adalah menjamin kepatuhan mutlak terhadap pedoman resmi UNNES 2026 dan catatan revisi Bimbingan 1.

---

## 🎯 Rubrik Audit Kualitas (Hierarki Evaluasi)

Prioritas evaluasi mengikuti urutan wajib:
$$\text{Validity} \longrightarrow \text{Feasibility} \longrightarrow \text{Relevance} \longrightarrow \text{Reproducibility} \longrightarrow \text{Novelty} \longrightarrow \text{Technical Precision}$$

Naskah **DITOLAK / WAJIB DIREVISI** apabila:
1. ❌ Ditemukan gambar atau diagram di Subbab 1.1 Latar Belakang (pelanggaran catatan revisi 5).
2. ❌ Jumlah Rumusan Masalah tidak tepat 3 butir atau tidak selaras dengan LightGBM/Optuna/TreeSHAP (pelanggaran catatan revisi 9).
3. ❌ Manfaat Penelitian tidak dibagi tepat menjadi 2 kategori (Teoretis dan Praktis) (pelanggaran catatan revisi 10).
4. ❌ Batasan Masalah tidak berbentuk poin-poin (*bullet points*) (pelanggaran catatan revisi 7).
5. ❌ Terdapat angka metrik, akurasi, atau dataset yang dikarang tanpa eksperimen nyata (*zero-hallucination failure*).
6. ❌ Gaya bahasa mengandung frasa AI klise (*anti-AI slop violation*).

---

## 📋 Checklist Audit per Subbab Proposal

### 1. Halaman Depan & Format Umum
- [ ] **Judul**: Kurang dari 20 kata (*Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna* — 17 kata).
- [ ] **Tipografi & Margin**: Font Times New Roman 12pt (Judul cover 14pt tebal), spasi 1.5, margin 4 cm kiri, 4 cm atas, 3 cm kanan, 3 cm bawah.
- [ ] **Sitasi & Referensi**: Format sitasi mematuhi APA Edisi ke-7 dengan DOI aktif.

### 2. Bab 1: Pendahuluan
- [ ] **1.1 Latar Belakang**:
  * Narasi deduktif: Fenomena kerugian industri asuransi akibat fraud (20-30% klaim, IAIS) → Masalah investigasi manual & tingginya Type II error → Kritik mendalam terhadap metode terdahulu (XGBoost komputasi berat, PSO lambat & rentan jebakan lokal) → Justifikasi LightGBM + Optuna Bayesian TPE + TreeSHAP.
  * **BEBAS DARI GAMBAR/DIAGRAM ALUR APAPUN**.
- [ ] **1.2 Batasan Masalah**:
  * Disajikan dalam bentuk poin-poin terstruktur (*bullet points*) membatasi objek, dataset (11.565 klaim), rasio imbalance (1:16), algoritma LightGBM-Optuna, baseline, metrik evaluasi, dan ruang lingkup keluaran.
- [ ] **1.3 Rumusan Masalah**:
  * Diawali paragraf pengantar singkat, lalu tepat **3 Research Questions (RQ)** yang spesifik pada LightGBM-Optuna, imbalance data, dan TreeSHAP.
- [ ] **1.4 Tujuan Penelitian**:
  * Tepat 3 butir yang berkorespondensi 1-to-1 dengan 3 RQ.
- [ ] **1.5 Manfaat Penelitian**:
  * Tepat 2 kategori: Manfaat Teoretis (keilmuan SI) dan Manfaat Praktis (industri asuransi & investigator fraud).
- [ ] **1.6 Kebaruan Penelitian**:
  * Memuat **Tabel 1.1 Penelitian Terdahulu yang Mendasari** (minimal 7 penelitian relevan termasuk Ding et al., 2025).
  * Menjelaskan pembeda utama: efisiensi LightGBM (GOSS/EFB), efektivitas Bayesian TPE Optuna, dan minimalisasi Type II error.

### 3. Bab 2: Kajian Pustaka
- [ ] **2.1 Tinjauan Pustaka**: Sintesis kritis studi deteksi fraud asuransi, perbandingan XGBoost vs LightGBM, serta evaluasi teknik optimasi (Grid Search, Random Search, PSO, Bayesian Optuna).
- [ ] **2.2 Landasan Teoretik**:
  * Konsep Asuransi Kendaraan Bermotor & Fraud Klaim.
  * Algoritma *Light Gradient Boosting Machine (LightGBM)*.
  * Optimasi Hyperparameter Bayesian via *Tree-structured Parzen Estimator (TPE)* dan framework Optuna.
  * Penanganan *Class Imbalance* pada Data Tabular.
  * Konsep *Explainable Artificial Intelligence (XAI)* dan TreeSHAP.
- [ ] **2.3 Kerangka Pemikiran**: Alur integrasi konseptual dari masalah bisnis asuransi hingga solusi model prediktif berbasis LightGBM-Optuna-TreeSHAP.

### 4. Bab 3: Metode Penelitian
- [ ] **3.1 Prosedur Penelitian**: Tahapan mengacu pada standar CRISP-DM (*Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment/Prototype*).
- [ ] **3.2 Sumber & Karakteristik Data**: Penjelasan eksplisit dataset sekunder 11.565 baris, 33 atribut, target `FraudFound_P`, rasio 1:16.
- [ ] **3.3 Pra-pemrosesan Data**: Penanganan missing value, Z-score scaling, dan penyeimbangan kelas (SMOTE / Random Resampling).
- [ ] **3.4 Desain Pemodelan & Optimasi Hyperparameter**: Spesifikasi ruang pencarian hyperparameter LightGBM dan konfigurasi Optuna TPE.
- [ ] **3.5 Metode Evaluasi & Interpretabilitas**: 5-Fold Stratified Cross-Validation, metrik Accuracy, Recall, Precision, F1-Score, Type II Error Rate, ROC-AUC, serta visualisasi TreeSHAP.

---

## 🛠️ Perintah Eksekusi Audit
Jalankan audit komprehensif pada dokumen `research/proposal.md` dengan memeriksa checklist di atas. Laporkan status:
* **[PASS]**: Memenuhi seluruh kriteria tanpa cacat.
* **[REVISE]**: Terdapat ketidakpatuhan minor (misal: format sitasi atau kalimat slop).
* **[FAIL]**: Terdapat pelanggaran fatal (misal: ada gambar di Latar Belakang, RQ > 3, atau manfaat > 2).
