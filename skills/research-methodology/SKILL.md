---
name: research-methodology
description: Panduan tahap awal penelitian untuk merumuskan Latar Belakang deduktif (tanpa gambar), Batasan Masalah dalam poin-poin, 3 Research Questions, dan 2 Manfaat Penelitian mengacu pada Bimbingan 1 dan Template UNNES 2026.
---

# Skill: Research Methodology (Tahap 1: Inisiasi & Formulasi Masalah)

Skill ini digunakan pada **Tahap 1 (Start)** untuk membangun fondasi ilmiah naskah proposal skripsi Bab 1 (Pendahuluan) berlandaskan perspektif Sistem Informasi dan instruksi ketat dosen pembimbing hasil Bimbingan 1.

---

## 🎯 Ground Truth & Constraint Kritis
Sesuai amanat [`project_context.md`](../../project_context.md) dan [`research_constraints.md`](../../research_constraints.md):
* **Judul**: *Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna* (17 kata).
* **Objek**: Klaim asuransi kendaraan bermotor (*automobile insurance fraud*).
* **Aturan Kritis Bimbingan 1**:
  1. ❌ **Latar Belakang DILARANG menggunakan gambar atau diagram** (*"lt bllkg gausah gambar"*).
  2. 🔍 **Masalah Utama**: Harus berakar pada telaah kritis data penelitian terdahulu mengenai metode yang digunakan, khususnya inefisiensi komputasi dan risiko konvergensi lokal pada optimasi hyperparameter (Grid Search / PSO pada XGBoost), serta rasio klaim fraud yang tinggi (20–30%).
  3. 📋 **Batasan Masalah**: WAJIB disajikan dalam bentuk poin-poin (*bullet points*).
  4. 🎯 **Rumusan Masalah**: WAJIB dibatasi tepat **3 Research Questions (RQ)** yang spesifik pada LightGBM, imbalance data, dan TreeSHAP.
  5. 💼 **Manfaat Penelitian**: WAJIB dibagi tepat menjadi **2 kategori** (Manfaat Teoretis dan Manfaat Praktis).
  6. ✨ **Kebaruan**: Diperbarui pada integrasi LightGBM + Optuna TPE + TreeSHAP di domain asuransi kendaraan.

---

## 🧭 Panduan Penyusunan Modul Riset

### 1. Modul `research/problem.md` (Subbab 1.1 Latar Belakang)
Susun narasi deduktif yang kokoh dengan alur piramida terbalik:
1. **Konteks Global Industri Asuransi Kendaraan**:
   * Asuransi kendaraan bermotor menyumbang 73%–80% dari total kasus fraud asuransi global/nasional.
   * Data IAIS: 20%–30% dari total klaim asuransi terindikasi curang, menggerus *underwriting profit* hingga puluhan triliun rupiah dan memicu kenaikan premi bagi nasabah jujur.
2. **Kelemahan Investigasi Manual**:
   * Volume klaim masif membuat investigasi manual mustahil dilakukan untuk 100% klaim.
   * Tingginya *Type II error* (klaim fraud gagal terdeteksi dan dibayarkan secara keliru).
3. **Kritik Metodologis Penelitian Terdahulu**:
   * Model klasik (SVM, Naive Bayes, Logistic Regression) memiliki akurasi rendah (54%–68%).
   * Model ensemble seperti XGBoost pada paper acuan Ding et al. (2025) berhasil mencapai akurasi 92%–95%, namun XGBoost memiliki beban komputasi dan konsumsi memori tinggi pada data tabular besar karena pembentukan histogram split eksak.
   * Optimasi hyperparameter menggunakan *Particle Swarm Optimization (PSO)* membutuhkan evaluasi fungsi objektif dalam jumlah iterasi partikel yang masif (50 partikel × 100 iterasi = 5000 evaluasi), berisiko konvergensi prematur pada ruang parameter campuran, serta lambat.
4. **Justifikasi Solusi yang Diajukan**:
   * **LightGBM**: Menggunakan *Gradient-based One-Side Sampling (GOSS)* dan *Exclusive Feature Bundling (EFB)*, menghasilkan kecepatan komputasi berkali-kali lipat lebih cepat dengan efisiensi memori tinggi tanpa mengorbankan akurasi.
   * **Optuna (TPE)**: Menggunakan Bayesian Optimization (*Tree-structured Parzen Estimator*) yang secara cerdas memodelkan probabilitas parameter terbaik berdasarkan trial sebelumnya dan mendukung *pruning* dini.
   * **TreeSHAP**: Memberikan transparansi interpretabilitas global dan lokal bagi investigator klaim.
   * **TIDAK ADA GAMBAR APAPUN DALAM LATAR BELAKANG**.

---

### 2. Modul `research/research-question.md`

#### Subbab 1.2 Batasan Masalah (Bulleted List)
Wajib memuat 7 poin batasan terstruktur:
* Objek data klaim asuransi kendaraan bermotor internasional (Kaggle/Oracle) dari paper acuan Ding et al. (2025).
* Dataset berukuran 11.565 baris, 33 atribut fitur, dan 1 variabel target biner `FraudFound_P`.
* Penanganan *class imbalance* ekstrem dengan rasio 1:16 (685 fraud vs 10.880 normal).
* Algoritma utama adalah LightGBM dengan optimasi hyperparameter Optuna (TPE).
* Baseline komparasi: XGBoost, PSO-XGBoost, Random Forest, Decision Tree, SVM, Naive Bayes.
* Metrik evaluasi berfokus pada Recall, F1-Score, ROC-AUC, dan penurunan *Type II error rate*.
* Output berupa model prediktif dan visualisasi interpretabilitas TreeSHAP (*decision support prototype*), tanpa integrasi *real-time core-banking*.

#### Subbab 1.3 Rumusan Masalah (Tepat 3 RQ)
* **RQ1**: Bagaimana kinerja model klasifikasi LightGBM yang dioptimasi menggunakan algoritma Optuna berbasis *Tree-structured Parzen Estimator (TPE)* dalam mendeteksi fraud klaim asuransi kendaraan bermotor dibandingkan dengan model baseline (XGBoost standar, PSO-XGBoost, Random Forest, dan SVM)?
* **RQ2**: Bagaimana pengaruh penerapan teknik penanganan *class imbalance* dan rekayasa fitur terhadap akurasi prediksi serta penurunan tingkat kesalahan *Type II error* (klaim fraud yang lolos teridentifikasi) pada model LightGBM-Optuna?
* **RQ3**: Bagaimana kontribusi dan signifikansi fitur-fitur klaim asuransi terhadap keluaran prediksi model yang diinterpretasikan menggunakan metode *TreeSHAP (SHapley Additive exPlanations)* untuk mendukung proses pengambilan keputusan investigasi klaim?

#### Subbab 1.4 Tujuan Penelitian
Tepat 3 butir yang selaras secara 1-to-1 dengan 3 RQ di atas.

#### Subbab 1.5 Manfaat Penelitian (Tepat 2 Kategori)
* **Manfaat Teoretis**: Kontribusi keilmuan Sistem Informasi terkait efektivitas LightGBM + Optuna TPE pada data tabular imbalanced dan interpretabilitas TreeSHAP.
* **Manfaat Praktis**: Rekomendasi manajerial dan *decision support* bagi tim investigator klaim perusahaan asuransi untuk triase klaim cepat dan meminimalkan kerugian finansial akibat fraud.

---

## ✅ Kriteria Verifikasi Tahap 1
- [ ] Dokumen `research/problem.md` bebas dari gambar/diagram alur.
- [ ] Masalah utama membedah kelemahan komputasi/konvergensi hyperparameter penelitian terdahulu.
- [ ] Batasan masalah berbentuk poin-poin terstruktur.
- [ ] Rumusan masalah terdiri tepat dari 3 Research Questions terukur.
- [ ] Manfaat penelitian terdiri tepat dari 2 kategori (Teoretis dan Praktis).
