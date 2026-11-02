# RESEARCH CONSTRAINTS & REVISI BIMBINGAN 1

Dokumen ini memetakan arahan dosen pembimbing hasil Bimbingan 1 (`bimbingan 1.txt`) ke dalam batasan dan spesifikasi teknis proposal skripsi. Seluruh agen, modul riset, dan naskah wajib mematuhi aturan ini secara ketat.

---

## 📌 Pemetaan Arahan Dosen Pembimbing

| No | Catatan Bimbingan (`bimbingan 1.txt`) | Interpretasi Akademis & Implementasi Teknis | Status Kepatuhan |
|---|---|---|---|
| 1 | `lgbm` | Algoritma klasifikasi utama beralih dari XGBoost ke **LightGBM (Light Gradient Boosting Machine)**. Memanfaatkan keunggulan *Gradient-based One-Side Sampling (GOSS)* dan *Exclusive Feature Bundling (EFB)* untuk efisiensi komputasi data tabular berskala besar. | Mandatory |
| 2 | `optuna lgbm` | Menggunakan **Optuna** sebagai framework optimasi hyperparameter untuk LightGBM dengan algoritma *Tree-structured Parzen Estimator (TPE)* berbasis Bayesian Optimization, menggantikan Particle Swarm Optimization (PSO) atau Grid Search. | Mandatory |
| 3 | `dataset dari paper acuan` | Menggunakan dataset klaim asuransi kendaraan bermotor (*Automobile Insurance Claim Fraud*) dari paper acuan Ding et al. (2025): **11.565 data klaim**, rasio fraud terhadap normal **1:16** (685 fraud vs 10.880 normal). | Mandatory |
| 4 | `bab 1 sesuaikan` | Menyesuaikan narasi Bab 1 (Pendahuluan) dari konteks *promotional abuse food delivery* menjadi **fraud klaim asuransi kendaraan bermotor (automobile insurance fraud)** dan arsitektur LightGBM + Optuna. | Mandatory |
| 5 | `lt bllkg gausah gambar` | Latar Belakang (Subbab 1.1) **TIDAK BOLEH** memuat gambar atau diagram alur. Seluruh argumentasi disajikan dalam bentuk narasi deduktif yang padat fakta, data empiris, dan sitasi bereputasi. | Mandatory |
| 6 | `maslah Utama data penelitian terdahulu terkait metode yang digunakan terkait hypermpamareter` | Masalah utama latar belakang berfokus pada evaluasi kritis metode penelitian terdahulu: keterbatasan penyetelan hyperparameter (manual/grid search boros komputasi, sedangkan PSO rentan terhadap konvergensi prematur pada ruang pencarian diskret/kontinu campuran), serta kebutuhan algoritma ensemble yang hemat memori dan cepat seperti LightGBM. | Mandatory |
| 7 | `Batasan masahlah berupa point2` | Subbab 1.2 Batasan Masalah **WAJIB** disusun dalam bentuk poin-poin (*bulleted list*) yang tegas, terukur, dan membatasi ruang lingkup (objek, dataset, metode, metrik, dan output). | Mandatory |
| 8 | `diperjelas dataset yang digunakan tool yang digunakan"` | Menyebutkan secara eksplisit detail dataset: 11.565 data transaksi klaim asuransi kendaraan (33 atribut/fitur, label biner `FraudFound_P`), rasio imbalanced 1:16, serta toolchain: Python 3.11+, LightGBM, Optuna, Scikit-learn, SHAP (TreeSHAP), Imbalanced-learn (SMOTE/Random Resampling), dan Pandas. | Mandatory |
| 9 | `rumusan maslaah 3 aja cukup disesuaikan lgbm nya` | Rumusan masalah (Subbab 1.3) dibatasi tepat **3 Research Questions (RQ)** yang menguji performa LightGBM-Optuna, penanganan class imbalance, dan interpretabilitas TreeSHAP. | Mandatory |
| 10 | `manfaat dibuat 2` | Subbab 1.5 Manfaat Penelitian dibatasi tepat **2 poin**: (1) Manfaat Teoretis (pengembangan keilmuan Sistem Informasi & data mining), dan (2) Manfaat Praktis (dukungan investigasi fraud bagi industri asuransi kendaraan). | Mandatory |
| 11 | `kebaharuan diuopdate, terkait ansurance` | Kebaruan penelitian (*Novelty Statement*) diperbarui pada domain asuransi kendaraan: integrasi LightGBM dengan Bayesian Optimization Optuna (TPE) dan TreeSHAP untuk mengatasi kelemahan model terdahulu (PSO-XGBoost pada Ding et al., 2025) dalam aspek efisiensi komputasi, penurunan Type II error (False Negative), dan interpretabilitas keputusan klaim. | Mandatory |

---

## 🚫 Larangan Keras (Negative Constraints)
1. **Dilarang memasukkan gambar di Latar Belakang**: Patuhi catatan revisi nomor 5.
2. **Dilarang menggunakan model selain LightGBM sebagai model usulan utama**: Model lain (XGBoost, Random Forest, SVM, Naive Bayes) hanya dijadikan baseline komparasi sesuai paper acuan.
3. **Dilarang mengarang data atau hasil evaluasi**: Semua angka metrik dalam eksperimen harus bersumber dari eksekusi nyata pada dataset acuan.
4. **Dilarang membuat Rumusan Masalah > 3 butir**: Pertahankan tepat 3 RQ selaras arahan bimbingan.
5. **Dilarang membuat Manfaat Penelitian > 2 kategori**: Pertahankan tepat 2 kategori (Teoretis dan Praktis).
