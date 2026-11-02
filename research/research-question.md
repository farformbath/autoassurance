# 1.2 Batasan Masalah

Guna menjaga fokus penelitian agar terarah, mendalam, dan terukur sesuai dengan koridor keilmuan Program Studi Sarjana Sistem Informasi, ruang lingkup penelitian ini dibatasi pada aspek-aspek sebagai berikut.

* **Objek data penelitian**: Data yang digunakan merupakan data transaksi klaim asuransi kendaraan bermotor (*automobile insurance claim fraud*) sekunder berstandar internasional (gabungan data investigasi fraud asuransi dan repositori Kaggle/Oracle) yang diadopsi langsung dari studi acuan Ding et al. (2025).
* **Ukuran dan dimensi data**: Dataset terdiri atas total 11.565 baris rekaman klaim dengan 33 atribut fitur penjelas (mencakup dimensi demografis nasabah, polis asuransi, karakteristik kendaraan, riwayat klaim lampau, dan detail kejadian kecelakaan) serta 1 atribut label target biner `FraudFound_P` (0 = klaim sah, 1 = klaim fraud).
* **Penanganan ketidakseimbangan kelas (*class imbalance*)**: Eksperimen berfokus pada penanganan distribusi data klaim yang terimbalans ekstrem dengan rasio 1:16 (685 klaim fraud berbanding 10.880 klaim normal), menggunakan teknik penyeimbangan data pada tingkat data (kombinasi *random under-sampling*, *random over-sampling*, dan SMOTE) serta penyesuaian bobot kelas (`scale_pos_weight`) pada tingkat algoritma.
* **Algoritma dan framework optimasi utama**: Algoritma klasifikasi utama yang dikembangkan adalah *Light Gradient Boosting Machine* (LightGBM), dengan optimasi hyperparameter otomatis berbasis optimasi Bayesian menggunakan framework Optuna melalui algoritma *Tree-structured Parzen Estimator* (TPE).
* **Model baseline pembanding**: Model pembanding dibatasi pada algoritma-algoritma yang digunakan dalam pengujian pada studi acuan Ding et al. (2025), yaitu *Extreme Gradient Boosting* (XGBoost standar), PSO-XGBoost, *Random Forest*, *Decision Tree*, *Support Vector Machine* (SVM), dan *Naive Bayes*.
* **Metrik evaluasi kinerja**: Evaluasi performa model diprioritaskan pada kemampuan mendeteksi kelas minoritas fraud, yang diukur menggunakan metrik *Recall*, *Precision*, *F1-Score*, *Area Under the Receiver Operating Characteristic Curve* (ROC-AUC), serta persentase penurunan tingkat kesalahan *Type II error* (*False Negative Rate* / klaim fraud yang lolos bayar).
* **Lingkup keluaran sistem (*deliverable scope*)**: Penelitian ini menghasilkan artefak berupa model prediktif teroptimasi dan modul visualisasi interpretabilitas menggunakan metode TreeSHAP (*SHapley Additive exPlanations*) sebagai prototipe sistem pendukung keputusan (*decision support prototype*) untuk analisis triase risiko klaim, tanpa mencakup integrasi langsung ke dalam sistem inti perbankan atau asuransi berskala produksi komersial.

---

# 1.3 Rumusan Masalah

Berdasarkan latar belakang masalah dan telaah kritis terhadap keterbatasan metode pada penelitian terdahulu, rumusan masalah dalam penelitian ini dirumuskan ke dalam 3 (tiga) pertanyaan penelitian (*Research Questions*) sebagai berikut.

1. **RQ1**: Bagaimana kinerja model klasifikasi *Light Gradient Boosting Machine* (LightGBM) yang dioptimasi menggunakan framework Optuna berbasis *Tree-structured Parzen Estimator* (TPE) dalam mendeteksi fraud klaim asuransi kendaraan bermotor jika dibandingkan dengan model baseline (XGBoost standar, PSO-XGBoost, Random Forest, dan SVM)?
2. **RQ2**: Bagaimana pengaruh penerapan teknik penanganan *class imbalance* (resampling/SMOTE) dan rekayasa fitur terhadap peningkatan akurasi serta penurunan tingkat kesalahan *Type II error* (klaim fraud yang gagal terdeteksi) pada model LightGBM-Optuna?
3. **RQ3**: Bagaimana kontribusi dan signifikansi fitur-fitur klaim asuransi kendaraan bermotor terhadap keluaran prediksi model yang diinterpretasikan menggunakan metode TreeSHAP (*SHapley Additive exPlanations*) dalam memberikan rekomendasi transparan bagi proses triase investigasi klaim?

---

# 1.4 Tujuan Penelitian

Selaras dengan rumusan masalah di atas, tujuan yang hendak dicapai dalam penelitian ini adalah sebagai berikut.

1. Menganalisis dan menguji peningkatan kinerja deteksi fraud klaim asuransi kendaraan bermotor menggunakan model LightGBM yang dioptimasi dengan algoritma Optuna berbasis *Tree-structured Parzen Estimator* (TPE) dibandingkan dengan model baseline pembelajaran mesin lainnya.
2. Mengevaluasi efektivitas penerapan strategi penanganan *class imbalance* dan rekayasa fitur dalam meminimalkan tingkat kesalahan *Type II error* (False Negative) dan memaksimalkan nilai *F1-Score* pada model LightGBM-Optuna.
3. Mengidentifikasi pola kontribusi dan urutan signifikansi fitur klaim terhadap prediksi fraud menggunakan analisis interpretabilitas TreeSHAP guna menghasilkan wawasan manajerial yang transparan bagi tim investigator klaim asuransi.

---

# 1.5 Manfaat Penelitian

Penelitian ini diharapkan dapat memberikan kontribusi nyata yang terbagi ke dalam 2 (dua) aspek manfaat sebagai berikut.

### 1. Manfaat Teoretis (Akademis)
* Memberikan kontribusi ilmiah pada ranah keilmuan sistem informasi, penambangan data (*data mining*), dan komputasi cerdas, khususnya mengenai efektivitas integrasi algoritma *Light Gradient Boosting Machine* (LightGBM) dan teknik optimasi hyperparameter Bayesian (Optuna TPE) dalam memecahkan masalah klasifikasi data tabular berdimensi tinggi dengan ketidakseimbangan kelas (*imbalanced data*) yang ekstrem di sektor finansial dan asuransi.
* Memperkaya khazanah penelitian mengenai penerapan *Explainable Artificial Intelligence* (XAI) menggunakan TreeSHAP dalam menjembatani kesenjangan antara kompleksitas model *ensemble learning* yang berkinerja tinggi dengan kebutuhan akuntabilitas dan interpretabilitas pada pengambilan keputusan bisnis (*decision-making transparency*).

### 2. Manfaat Praktis (Industri & Manajerial)
* Menjadi acuan teknis dan instrumen pendukung keputusan (*decision support tool*) bagi manajemen risiko perusahaan asuransi umum serta tim penilai klaim (*claims investigators / fraud analysts*) untuk mengotomatisasi proses triase klaim masuk secara lebih cepat, objektif, dan terukur.
* Membantu memitigasi kerugian finansial perusahaan asuransi akibat pembayaran klaim curang yang tidak terdeteksi (*Type II error*), sekaligus melindungi hak nasabah yang sah dari hambatan atau keterlambatan pencairan santunan klaim (*Type I error*), sehingga berdampak langsung pada perbaikan rasio laba *underwriting* dan menjaga kepuasan konsumen.
