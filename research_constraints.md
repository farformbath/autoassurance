# RESEARCH CONSTRAINTS & REVISI BIMBINGAN

Dokumen ini memetakan seluruh arahan dan catatan revisi dosen pembimbing dari tiga sumber:
1. **Catatan Bimbingan 1 (`bimbingan 1.txt`)**: Pergeseran topik ke artikel acuan Ding et al. (2025) dan metode LightGBM-Optuna.
2. **Catatan Redaksional Dosen Pembimbing (`revisi.md`)**: Standar gaya penulisan, struktur logika Latar Belakang, tipografi, dan tata bahasa baku naskah.
3. **Mandat Kemutakhiran Pustaka (2021++ & Verified DOI)**: Standar integritas sitasi ilmiah terindeks tanpa rujukan fiktif.

Seluruh agen, modul riset, dan naskah wajib mematuhi aturan ini secara ketat.

---

## 📌 Bagian 1: Pemetaan Arahan Substantif Bimbingan 1 (`bimbingan 1.txt`)

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

## ✍️ Bagian 2: Aturan Redaksional, Logika Penulisan & Pustaka

| No | Aturan Redaksional & Pustaka | Aturan Teknis & Larangan Penulisan | Contoh Implementasi yang Benar |
|---|---|---|---|
| 1 | `gap harus dieksplisit di abb 1.1` | **Kesenjangan penelitian (*research gap*) wajib dinyatakan secara eksplisit** pada Subbab 1.1 dengan kalimat deklaratif yang jelas, bukan sekadar tersirat di akhir bab. | *"Kesenjangan penelitian (research gap) yang menjadi fokus utama dalam penelitian ini terletak pada..."* |
| 2 | `1.1 JANGAN PENGGUNAAN xgbos=ost untuk apa apa apa...` | **Latar Belakang bukan tempat memaparkan implementasi solusi.** Dilarang langsung menulis *"Penggunaan LightGBM untuk..."*. Latar Belakang harus murni mengurai fenomena masalah bisnis, kelemahan penanganan manual, kritik atas metode penelitian terdahulu, dan memformulasikan *research gap*. | Awali dengan masalah kerugian klaim asuransi, kelemahan investigator manual, baru menelaah keterbatasan metode terdahulu. |
| 3 | `model riskscooring seperti aoa... kata kunci di judul harus muncul pada bab 1.1` | **Seluruh kata kunci pada judul WAJIB muncul dan dibahas secara konseptual di Subbab 1.1**, agar terdapat benang merah yang konsisten dari Bab 1 menuju Bab 3 (misal: *fraud klaim asuransi kendaraan, LightGBM, optimasi hyperparameter Optuna, sistem pendukung keputusan*). | Setiap konsep utama didefinisikan perannya dalam alur penanganan fraud asuransi. |
| 4 | `penulisan istilah tidak perlu tittle case, (akronim ditulis capital)` | **Istilah teknis dalam kalimat narasi biasa DILARANG menggunakan Title Case** (huruf besar di awal kata). Huruf kapital hanya untuk awal kalimat, nama diri, dan AKRONIM singkatan. | ✅ *sistem pendukung keputusan*, *optimasi hyperparameter*, *penambangan data*.<br>❌ *Sistem Pendukung Keputusan*, *Optimasi Hyperparameter*. |
| 5 | `kalo singkatan kedepannya tidak dipakai tidak perlu disingkat` | **Dilarang membuat singkatan jika istilah tersebut tidak digunakan berulang kali** pada paragraf berikutnya. Tuliskan nama lengkapnya saja. | Jika hanya disebut 1 kali, tulis *service level agreement* (jangan buat singkatan *SLA* jika tidak pernah dipakai lagi). |
| 6 | `Bahasa Indonesia inggris pilih salah satu jangan berkali kali` | **Konsistensi bahasa istilah asing**: Pilih satu istilah dan pertahankan secara konsisten. Istilah asing wajib dicetak miring (*italics*). Jangan bergantian memanggil objek yang sama dengan istilah Indonesia lalu Inggris secara acak. | Gunakan konsisten: *fraud klaim* atau *klaim curang* (pilih satu, jangan campur aduk). |
| 7 | `no repitasi` | **Zero Redundancy**: Dilarang mengulang kalimat, ide, atau fakta yang sama pada paragraf yang berdekatan. Setiap paragraf harus membawa argumen baru. | Setiap paragraf memiliki satu *topic sentence* yang unik. |
| 8 | `sebgai berikut. tnada titik bukan : tanda titik dua` | **Tanda baca sebelum perincian daftar/poin**: Frasa pengantar *"sebagai berikut."* **WAJIB MENGGUNAKAN TANDA TITIK (.)**, DILARANG menggunakan tanda titik dua (:). | ✅ *"dirumuskan ke dalam 3 pertanyaan penelitian sebagai berikut."*<br>❌ *"...sebagai berikut:"* |
| 9 | **Mandat Kemutakhiran Pustaka (2021++ & Verified DOI)** | **Seluruh artikel jurnal empiris pendukung WAJIB terbitan tahun 2021 ke atas (2021++)** dari penerbit bereputasi (Elsevier, IEEE, Springer, Wiley) dengan **DOI aktif yang dapat dilacak secara nyata di CrossRef/doi.org**. Pengecualian tahun hanya berlaku untuk *seminal papers* penemu algoritma dasar (Ke et al. 2017 LightGBM, Akiba et al. 2019 Optuna, Lundberg et al. 2020 TreeSHAP, Chen & Guestrin 2016 XGBoost, Chawla et al. 2002 SMOTE, Chapman et al. 2000 CRISP-DM). Dilarang keras menggunakan sitasi fiktif (*zero hallucinated citations*). | Ding et al. (2025) DOI: 10.1016/j.insmatheco.2024.11.006, Nordin et al. (2024) DOI: 10.11591/ijece.v14i1.pp911-921, Maiano et al. (2023) DOI: 10.1016/j.eswa.2023.120644. |

---

## 🚫 Larangan Keras Gabungan (Negative Constraints)
1. **Dilarang memasukkan gambar di Latar Belakang**: Patuhi catatan `bimbingan 1.txt` poin 5.
2. **Dilarang menggunakan tanda titik dua (:) setelah "sebagai berikut."**: Wajib gunakan tanda titik (.).
3. **Dilarang menggunakan Title Case pada kata-kata narasi biasa**: Hanya akronim yang ditulis kapital.
4. **Dilarang membuat Rumusan Masalah > 3 butir**: Pertahankan tepat 3 RQ selaras arahan bimbingan.
5. **Dilarang membuat Manfaat Penelitian > 2 kategori**: Pertahankan tepat 2 kategori (Teoretis dan Praktis).
6. **Dilarang mengarang data atau angka metrik**: Wajib merujuk pada hasil eksekusi nyata dataset di `data/`.
7. **Dilarang menggunakan referensi fiktif atau jurnal empiris usang (< 2021)**: Seluruh jurnal studi komparasi fraud asuransi wajib 2021++ dengan DOI aktif yang terverifikasi.
