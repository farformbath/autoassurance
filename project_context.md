# PROJECT CONTEXT

## 1. Identitas Penelitian
* **Judul Penelitian**: *Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna*
* **Jumlah Kata Judul**: 17 kata (memenuhi syarat UNNES: < 20 kata).
* **Program Studi**: Sarjana Sistem Informasi, FMIPA Universitas Negeri Semarang (UNNES).
* **Tahun Akademik**: 2026.
* **Artikel Acuan Utama**:  
  Ding, N., Ruan, X., Wang, H., & Liu, Y. (2025). Automobile insurance fraud detection based on PSO-XGBoost model and interpretable machine learning method. *Insurance Mathematics and Economics*, 120, 51–60. https://doi.org/10.1016/j.insmatheco.2024.11.006

---

## 2. Bidang & Karakteristik Penelitian
* **Bidang Ilmu**: Sistem Informasi (Integrasi *Technology, People, Process, Organization*).
* **Jenis Penelitian**: Penelitian pengembangan model prediktif berbasis *Machine Learning* dan *Decision Support System (DSS)*.
* **Pendekatan Metodologi**: CRISP-DM (*Cross-Industry Standard Process for Data Mining*).

---

## 3. Fenomena & Problem Statement
### Fenomena Bisnis & Empiris:
* Asuransi kendaraan bermotor (*automobile insurance*) merupakan pilar utama sektor asuransi umum, namun menyumbang sekitar 73% hingga 80% dari total kasus fraud asuransi yang dilaporkan.
* *International Association of Insurance Supervisors (IAIS)* mengestimasi 20% hingga 30% dari total klaim asuransi terindikasi mencurigakan/fraud, mengakibatkan lonjakan beban klaim, depresiasi *underwriting profit*, dan terpaksa menaikkan premi bagi pemegang polis jujur.
* Investigasi manual terhadap seluruh klaim tidak realistis karena keterbatasan sumber daya manusia investigator dan tingginya volume klaim harian, sehingga memicu tingginya *Type II error* (klaim fraud gagal terdeteksi dan dibayarkan).

### Masalah Utama Terkait Metode Penelitian Terdahulu (Kritik Literatur):
* **Keterbatasan Algoritma Pembelajaran Mesin Konvensional & XGBoost**: Model seperti SVM, Naive Bayes, dan Logistic Regression menghasilkan akurasi rendah (54%–68%). Meskipun XGBoost menghasilkan performa tinggi, algoritma ini membutuhkan waktu komputasi besar dan memori tinggi karena membangun histogram split secara penuh. Sebaliknya, **LightGBM** menerapkan mekanisme *Gradient-based One-Side Sampling (GOSS)* dan *Exclusive Feature Bundling (EFB)* yang mampu mempercepat proses pelatihan hingga beberapa kali lipat dengan efisiensi memori lebih tinggi pada data tabular besar.
* **Kelemahan Penyetelan Hyperparameter PSO vs Bayesian Optimization (Optuna)**: Penelitian acuan Ding et al. (2025) menggunakan *Particle Swarm Optimization (PSO)*. PSO membutuhkan evaluasi fungsi objektif dalam jumlah iterasi partikel yang besar (50 partikel × 100 iterasi = 5000 evaluasi model), rentan terhadap *premature convergence* (terjebak pada local optima) pada ruang pencarian kontinu-diskret campuran, dan tidak memanfaatkan riwayat probabilitas secara formal. **Optuna** dengan algoritma *Tree-structured Parzen Estimator (TPE)* memodelkan distribusi probabilitas hyperparameter terdahulu secara Bayesian, mengeksplorasi ruang parameter secara jauh lebih cerdas, efisien, serta mendukung mekanisme pemangkasan (*pruning*) otomatis pada trial yang tidak menjanjikan.
* **Kebutuhan Interpretabilitas Transparan**: Model berbasis pohon sering dianggap *black-box*. Investigator asuransi membutuhkan justifikasi berbasis *Explainable AI (XAI)* melalui TreeSHAP untuk memahami faktor dominan (seperti *ClaimSize, VehicleCategory, Fault, Age*) dalam proses triase klaim.

---

## 4. Perspektif Sistem Informasi
Model tidak berdiri sendiri sebagai kode semata, melainkan dirancang sebagai komponen solusi sosioteknis:
* **Technology**: LightGBM, Optuna (TPE), TreeSHAP, Python, Scikit-learn, Imbalanced-learn.
* **People**: Investigator klaim (*fraud analysts*), manajemen risiko asuransi, dan pemegang polis sah.
* **Process**: Alur penerimaan klaim, verifikasi otomatis berjenjang (triase risiko), dan audit investigasi mendalam pada klaim berisiko tinggi.
* **Organization**: Perusahaan asuransi umum (*general insurance*), badan pengawas asuransi (OJK), dan kepolisian/investigasi legal.

---

## 5. Batasan Masalah (Bulleted List)
Sesuai arahan bimbingan, batasan masalah dirumuskan secara tegas dalam bentuk poin-poin:
1. **Objek Penelitian**: Data transaksi klaim asuransi kendaraan bermotor (*automobile insurance claims*) sekunder dari repositori publik internasional (Kaggle/Oracle) yang diadopsi dari paper acuan Ding et al. (2025).
2. **Karakteristik Dataset**: Terdiri dari 11.565 baris data klaim dengan 33 atribut penjelas (fitur demografis, kebijakan polis, kendaraan, riwayat klaim, dan kondisi kecelakaan) serta 1 variabel target biner `FraudFound_P` (0 = klaim sah, 1 = klaim fraud).
3. **Kondisi Data Imbalance**: Dataset memiliki ketidakseimbangan kelas ekstrem (rasio fraud terhadap sah sekitar 1:16; 685 klaim fraud vs 10.880 klaim normal), ditangani menggunakan teknik *resampling* (kombinasi random under-sampling/over-sampling atau SMOTE) dan penyesuaian bobot kelas (`scale_pos_weight`).
4. **Algoritma & Framework Optimasi**: Model utama menggunakan **LightGBM**, dengan optimasi hyperparameter otomatis berbasis Bayesian Optimization menggunakan **Optuna (TPE)**.
5. **Model Pembanding (Baseline)**: Model pembanding dibatasi pada algoritma yang diuji dalam paper acuan, yaitu XGBoost standar, PSO-XGBoost, Random Forest, Decision Tree, SVM, dan Naive Bayes.
6. **Metrik Evaluasi**: Difokuskan pada akurasi klasifikasi kelas minoritas, meliputi Recall, Precision, F1-Score, ROC-AUC, PR-AUC, serta penurunan persentase *Type II error rate* (False Negative Rate / klaim fraud yang lolos).
7. **Lingkup Keluaran Sistem**: Penelitian menghasilkan model prediksi risiko dan modul analisis interpretabilitas TreeSHAP (*global & local explanation*) sebagai sistem pendukung keputusan (*decision support prototype*), tanpa mencakup integrasi *core insurance system* produksi perbankan/asuransi secara *real-time*.

---

## 6. Rumusan Masalah (Tepat 3 Butir)
1. **RQ1**: Bagaimana kinerja model klasifikasi LightGBM yang dioptimasi menggunakan algoritma Optuna berbasis *Tree-structured Parzen Estimator (TPE)* dalam mendeteksi fraud klaim asuransi kendaraan bermotor dibandingkan dengan model baseline (XGBoost standar, PSO-XGBoost, Random Forest, dan SVM)?
2. **RQ2**: Bagaimana pengaruh penerapan teknik penanganan *class imbalance* dan rekayasa fitur terhadap akurasi prediksi serta penurunan tingkat kesalahan *Type II error* (klaim fraud yang lolos teridentifikasi) pada model LightGBM-Optuna?
3. **RQ3**: Bagaimana kontribusi dan signifikansi fitur-fitur klaim asuransi terhadap keluaran prediksi model yang diinterpretasikan menggunakan metode *TreeSHAP (SHapley Additive exPlanations)* untuk mendukung proses pengambilan keputusan investigasi klaim?

---

## 7. Tujuan Penelitian (Selaras 3 Butir)
1. Menganalisis dan menguji peningkatan kinerja deteksi fraud klaim asuransi kendaraan bermotor menggunakan model LightGBM yang dioptimasi dengan algoritma Optuna (TPE) dibandingkan model baseline.
2. Mengevaluasi dampak strategi penanganan *class imbalance* dan rekayasa fitur dalam meminimalkan *Type II error* (False Negative) dan memaksimalkan F1-score pada model LightGBM-Optuna.
3. Mengidentifikasi pola dan signifikansi fitur-fitur klaim paling berpengaruh terhadap indikasi fraud menggunakan interpretabilitas TreeSHAP guna memberikan rekomendasi transparan bagi investigator klaim asuransi.

---

## 8. Manfaat Penelitian (Tepat 2 Poin)
1. **Manfaat Teoretis**:
   * Memberikan kontribusi akademis pada bidang Sistem Informasi dan *data mining*, khususnya mengenai efektivitas integrasi algoritma *Light Gradient Boosting Machine* dengan *Bayesian Hyperparameter Optimization (Optuna TPE)* dalam menangani permasalahan data tabular berdimensi tinggi dengan *class imbalance* ekstrem pada sektor asuransi.
   * Memperkaya kajian literatur mengenai penerapan *Explainable AI (XAI)* menggunakan TreeSHAP pada industri keuangan untuk menjembatani kesenjangan antara akurasi model *ensemble learning* yang kompleks dengan kebutuhan transparansi manajerial (*black-box vs white-box trade-off*).
2. **Manfaat Praktis**:
   * Menjadi acuan dan alat bantu pendukung keputusan (*decision support*) bagi perusahaan asuransi umum, manajer risiko, dan tim investigator klaim (*fraud analysts*) untuk melakukan triase klaim secara cepat, akurat, dan objektif.
   * Membantu meminimalkan kerugian finansial perusahaan akibat pembayaran klaim curang (*Type II error*) sekaligus melindungi nasabah beritikad baik dari keterlambatan pencairan klaim sah (*Type I error*), sehingga menjaga stabilitas rasio klaim dan *underwriting profit*.

---

## 9. Kebaruan Penelitian (Novelty Statement)
Berbeda dengan penelitian acuan terdahulu oleh Ding et al. (2025) yang menggunakan kombinasi *Particle Swarm Optimization* dan *Extreme Gradient Boosting (PSO-XGBoost)* dengan kelemahan waktu komputasi yang tinggi serta risiko konvergensi lokal, kebaruan penelitian ini terletak pada:
1. Penerapan arsitektur **LightGBM** yang memanfaatkan mekanisme GOSS dan EFB untuk pemrosesan data tabular klaim asuransi yang lebih efisien dan terukur secara komputasi.
2. Pemanfaatan framework optimasi **Optuna berbasis Bayesian TPE (Tree-structured Parzen Estimator)** yang mengeksplorasi ruang hyperparameter secara adaptif dan terarah berdasarkan probabilitas riwayat trial, menghasilkan konvergensi parameter yang lebih cepat dan optimal dibanding algoritma heuristik PSO.
3. Integrasi menyeluruh antara optimasi hyperparameter Bayesian, strategi penanganan ketidakseimbangan kelas (1:16) berorientasi minimalisasi *Type II error*, dan visualisasi interpretabilitas TreeSHAP multi-level (*feature importance, summary plot, dependency interaction*) yang dirancang khusus untuk kebutuhan triase operasional klaim asuransi kendaraan bermotor.

---

## 10. Spesifikasi Teknis & Toolchain
* **Bahasa Pemrograman**: Python 3.11+
* **Core Libraries**:
  * `lightgbm` (>= 4.0.0): Algoritma *Light Gradient Boosting Machine*.
  * `optuna` (>= 3.5.0): Framework optimasi hyperparameter Bayesian (TPE).
  * `xgboost` (>= 2.0.0): Baseline perbandingan paper acuan.
  * `shap` (>= 0.44.0): Analisis interpretabilitas TreeSHAP.
  * `scikit-learn` (>= 1.4.0): Metrik evaluasi, cross-validation, preprocessing, baseline models (RF, DT, SVM, NB, LR).
  * `imbalanced-learn` (>= 0.12.0): Teknik resampling (Random Under/Over Sampling, SMOTE).
  * `pandas`, `numpy`: Manipulasi data tabular dan kalkulasi matriks.
  * `matplotlib`, `seaborn`: Visualisasi performa, kurva ROC/PR, dan plot SHAP.
* **Format Penulisan**: Naskah Markdown (`research/*.md`) yang dapat dikompilasi menjadi naskah Word (`.docx`) sesuai *Template Resmi Proposal Skripsi UNNES 2026*.
