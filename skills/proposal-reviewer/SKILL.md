---
name: proposal-reviewer
description: Panduan tahap akhir (End) untuk audit kualitas, validasi struktur naskah Bab 1, 2, dan 3, serta verifikasi kepatuhan terhadap Template Resmi Proposal Skripsi UNNES 2026, 11 poin revisi Bimbingan 1, dan 8 aturan redaksional revisi.md.
---

# Skill: Proposal Reviewer (Tahap 4: Review & Audit Kualitas Naskah)

Skill ini digunakan pada **Tahap Akhir (End)** sebelum naskah proposal skripsi diajukan ke dosen pembimbing atau seminar proposal. Fokusnya adalah menjamin kepatuhan mutlak terhadap pedoman resmi UNNES 2026, catatan revisi Bimbingan 1 (`bimbingan 1.txt`), dan catatan redaksional (`revisi.md`).

---

## 🎯 Rubrik Audit Kualitas (Hierarki Evaluasi)

Prioritas evaluasi mengikuti urutan wajib:
$$\text{Validity} \longrightarrow \text{Feasibility} \longrightarrow \text{Relevance} \longrightarrow \text{Reproducibility} \longrightarrow \text{Novelty} \longrightarrow \text{Technical Precision}$$

Naskah **DITOLAK / WAJIB DIREVISI** apabila:
1. ❌ Ditemukan gambar atau diagram di Subbab 1.1 Latar Belakang (pelanggaran bimbingan 1 poin 5).
2. ❌ Terdapat tanda titik dua (:) setelah frasa *"sebagai berikut."* (wajib menggunakan tanda titik `.`, pelanggaran `revisi.md` poin 8).
3. ❌ Penggunaan Title Case (huruf besar di awal kata) pada istilah umum narasi biasa (pelanggaran `revisi.md` poin 4).
4. ❌ Jumlah Rumusan Masalah tidak tepat 3 butir atau tidak selaras dengan LightGBM/Optuna/TreeSHAP (pelanggaran bimbingan 1 poin 9).
5. ❌ Manfaat Penelitian tidak dibagi tepat menjadi 2 kategori (Teoretis dan Praktis) (pelanggaran bimbingan 1 poin 10).
6. ❌ Batasan Masalah tidak berbentuk poin-poin (*bullet points*) (pelanggaran bimbingan 1 poin 7).
7. ❌ Kesenjangan penelitian (*research gap*) tidak dinyatakan secara eksplisit pada Subbab 1.1 (pelanggaran `revisi.md` poin 1).
8. ❌ Terdapat repetisi kalimat atau frasa asing yang campur aduk tidak konsisten (pelanggaran `revisi.md` poin 6 & 7).
9. ❌ Terdapat angka metrik, akurasi, atau dataset yang dikarang tanpa eksperimen nyata (*zero-hallucination failure*).
10. ❌ Gaya bahasa mengandung frasa AI klise (*anti-AI slop violation*).

---

## 📋 Checklist Audit per Subbab Proposal

### 1. Halaman Depan & Format Umum
- [ ] **Judul**: Kurang dari 20 kata (*Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna* — 17 kata).
- [ ] **Tipografi & Margin**: Font Times New Roman 12pt (Judul cover 14pt tebal), spasi 1.5, margin 4 cm kiri, 4 cm atas, 3 cm kanan, 3 cm bawah.
- [ ] **Sitasi & Referensi**: Format sitasi mematuhi APA Edisi ke-7 dengan DOI aktif.

### 2. Bab 1: Pendahuluan
- [ ] **1.1 Latar Belakang**:
  * Narasi deduktif murni: Kerugian industri asuransi (20-30% fraud, IAIS) $\to$ Kelemahan investigasi manual & Type II error $\to$ Kritik metode terdahulu (XGBoost komputasi berat, PSO rentan jebakan lokal) $\to$ Research gap eksplisit $\to$ Justifikasi LightGBM + Optuna TPE + TreeSHAP.
  * **BEBAS DARI GAMBAR/DIAGRAM ALUR APAPUN**.
  * **Research gap dinyatakan secara eksplisit** (memuat kalimat lugas perumusan celah riset).
  * Seluruh kata kunci judul dibahas perannya secara konseptual.
  * Tidak terburu-buru menyimpulkan implementasi solusi sebelum mengurai masalah.
- [ ] **1.2 Batasan Masalah**:
  * Disajikan dalam bentuk poin-poin terstruktur (*bullet points*) membatasi objek, dataset (11.565 klaim), rasio imbalance (1:16), algoritma LightGBM-Optuna, baseline, metrik evaluasi, dan ruang lingkup keluaran.
  * Menggunakan pengantar *"sebagai berikut."* dengan tanda titik (bukan titik dua `:`).
- [ ] **1.3 Rumusan Masalah**:
  * Diawali paragraf pengantar singkat, lalu tepat **3 Research Questions (RQ)** yang spesifik pada LightGBM-Optuna, imbalance data, dan TreeSHAP.
  * Menggunakan pengantar *"sebagai berikut."* dengan tanda titik.
- [ ] **1.4 Tujuan Penelitian**:
  * Tepat 3 butir yang berkorespondensi 1-to-1 dengan 3 RQ.
  * Menggunakan pengantar *"sebagai berikut."* dengan tanda titik.
- [ ] **1.5 Manfaat Penelitian**:
  * Tepat 2 kategori: Manfaat Teoretis (keilmuan SI) dan Manfaat Praktis (industri asuransi & investigator fraud).
  * Menggunakan pengantar *"sebagai berikut."* dengan tanda titik.
- [ ] **1.6 Kebaruan Penelitian**:
  * Memuat **Tabel 1.1 Penelitian Terdahulu yang Mendasari** (minimal 7 penelitian relevan termasuk Ding et al., 2025).
  * Menjelaskan pembeda utama: efisiensi LightGBM (GOSS/EFB), efektivitas Bayesian TPE Optuna, dan minimalisasi Type II error.

### 3. Kaidah Kebahasaan & Redaksional (`revisi.md`)
- [ ] **Tanda Baca**: Seluruh kalimat pengantar daftar menggunakan *"sebagai berikut."* bertanda titik.
- [ ] **Kapitalisasi / Title Case**: Kata-kata narasi biasa ditulis huruf kecil (misal: *sistem pendukung keputusan*, *penambangan data*, *optimasi hyperparameter*). Huruf kapital HANYA untuk nama diri, awal kalimat, dan AKRONIM (`LightGBM`, `XGBoost`, `Optuna`, `TPE`, `PSO`, `SHAP`, `SMOTE`).
- [ ] **Singkatan Efisien**: Tidak ada singkatan di dalam kurung jika tidak digunakan berulang kali di paragraf berikutnya.
- [ ] **Konsistensi Bahasa**: Istilah asing dicetak miring (*italics*) dan tidak bergantian secara acak dengan bahasa Indonesia untuk objek yang sama.
- [ ] **Zero Redundancy**: Tidak ada pengulangan kalimat, ide, atau fakta yang sama pada paragraf berdekatan.

### 4. Bab 2: Kajian Pustaka
- [ ] **2.1 Tinjauan Pustaka**: Sintesis kritis studi deteksi fraud asuransi, perbandingan XGBoost vs LightGBM, serta evaluasi teknik optimasi (Grid Search, Random Search, PSO, Bayesian Optuna).
- [ ] **2.2 Landasan Teoretik**:
  * Konsep Asuransi Kendaraan Bermotor & Fraud Klaim.
  * Algoritma *Light Gradient Boosting Machine (LightGBM)*.
  * Optimasi Hyperparameter Bayesian via *Tree-structured Parzen Estimator (TPE)* dan framework Optuna.
  * Penanganan *Class Imbalance* pada Data Tabular.
  * Konsep *Explainable Artificial Intelligence (XAI)* dan TreeSHAP.
- [ ] **2.3 Kerangka Pemikiran**: Alur integrasi konseptual dari masalah bisnis asuransi hingga solusi model prediktif berbasis LightGBM-Optuna-TreeSHAP.

### 5. Bab 3: Metode Penelitian
- [ ] **3.1 Prosedur Penelitian**: Tahapan mengacu pada standar CRISP-DM (*Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment/Prototype*).
- [ ] **3.2 Sumber & Karakteristik Data**: Penjelasan eksplisit dataset sekunder 11.565 baris, 33 atribut, target `FraudFound_P`, rasio 1:16.
- [ ] **3.3 Pra-pemrosesan Data**: Penanganan missing value, Z-score scaling, dan penyeimbangan kelas (SMOTE / Random Resampling).
- [ ] **3.4 Desain Pemodelan & Optimasi Hyperparameter**: Spesifikasi ruang pencarian hyperparameter LightGBM dan konfigurasi Optuna TPE.
- [ ] **3.5 Metode Evaluasi & Interpretabilitas**: 5-Fold Stratified Cross-Validation, metrik Accuracy, Recall, Precision, F1-Score, Type II Error Rate, ROC-AUC, serta visualisasi TreeSHAP.

---

## 🛠️ Perintah Eksekusi Audit
Jalankan audit komprehensif pada dokumen naskah dengan memeriksa checklist di atas. Laporkan status:
* **[PASS]**: Memenuhi seluruh kriteria tanpa cacat.
* **[REVISE]**: Terdapat ketidakpatuhan minor (misal: format sitasi atau inkonsistensi miring).
* **[FAIL]**: Terdapat pelanggaran fatal (misal: ada gambar di Latar Belakang, RQ > 3, manfaat > 2, atau tanda titik dua setelah "sebagai berikut.").
