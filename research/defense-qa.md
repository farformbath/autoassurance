# Panduan Pertahanan Seminar Proposal (Defense Q&A Guide)

> **Judul Penelitian**: Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna  
> **Program Studi**: Sarjana Sistem Informasi, FMIPA Universitas Negeri Semarang (UNNES)  
> **Peneliti**: Irfan Fatkhurrizal (NIM: 2404140090)

---

## 🎯 Prinsip Utama Menjawab Pertanyaan Dewan Penguji

1. **Pembedaan Tegas Antara Fakta dan Rencana**:
   * *Evidence terverifikasi*: Data statistik IAIS (20–30% fraud), karakteristik dataset sekunder acuan Ding et al. 2025 (11.565 klaim, rasio 1:16, 33 atribut).
   * *Rencana metodologi*: Pipeline CRISP-DM, Stratified 5-Fold Cross-Validation, optimasi Bayesian TPE via Optuna, dan analisis interpretabilitas TreeSHAP.
   * *Hasil eksperimen*: Menolak klaim performa apriori (*over-claim*) seperti "pasti akurat 100%" sebelum eksperimen selesai dijalankan.
2. **Keterkaitan Sistem Informasi (Sosioteknis)**:
   * Menjelaskan model bukan sekadar kode/script, melainkan sistem pendukung keputusan (*decision support system*) yang menghubungkan *Technology* (LightGBM & Optuna), *People* (Investigator klaim asuransi), *Process* (Alur triase klaim masuk), dan *Organization* (Manajemen risiko perusahaan asuransi umum).

---

## 💬 Bank Pertanyaan Kunci Penguji & Rekomendasi Jawaban Ilmiah

### 1. Pertanyaan: Mengapa memilih algoritma LightGBM dan bukan XGBoost seperti pada paper acuan Ding et al. (2025) atau Deep Learning?
* **Rekomendasi Jawaban**:
  > *"Terima kasih atas pertanyaannya, Bapak/Ibu Dewan Penguji. Pemilihan LightGBM didasarkan pada dua pertimbangan ilmiah dan teknis utama:*
  >
  > *Pertama, **karakteristik data klaim asuransi adalah data tabular terstruktur berskala besar**. Literatur komparatif internasional membuktikan bahwa model ensemble pohon keputusan secara konsisten lebih unggul dan efisien dibanding deep learning pada data tabular heterogen.*
  >
  > *Kedua, **keunggulan komputasi struktural LightGBM dibanding XGBoost**. Pada paper acuan Ding et al. (2025), XGBoost menggunakan algoritma exact greedy scan yang memindai seluruh data dan fitur untuk membentuk split pohon, sehingga memerlukan alokasi memori besar dan waktu latih lama. Sebaliknya, **LightGBM memperkenalkan dua teknik inovatif**: (1) Gradient-based One-Side Sampling (GOSS) yang mempertahankan sampel bergradien besar dan menyampling sampel bergradien kecil, serta (2) Exclusive Feature Bundling (EFB) yang menggabungkan fitur-fitur kategorikal yang jarang. Hal ini membuat LightGBM mampu melatih model hingga berkali-kali lipat lebih cepat dengan konsumsi memori yang jauh lebih rendah tanpa mengorbankan akurasi prediksi kelas fraud."*

---

### 2. Pertanyaan: Mengapa Anda mengganti metode optimasi Particle Swarm Optimization (PSO) pada paper acuan dengan Optuna?
* **Rekomendasi Jawaban**:
  > *"Terima kasih atas pertanyaannya. Pada penelitian acuan Ding et al. (2025), optimasi hyperparameter XGBoost menggunakan algoritma PSO. Berdasarkan telaah kritis kami, PSO memiliki tiga kelemahan mendasar:*
  >
  > *1. **Beban komputasi yang sangat mahal**: Peneliti acuan menggunakan 50 partikel dan 100 iterasi, yang berarti model harus dilatih ulang sebanyak 5.000 kali pengujian.*
  > *2. **Rentan terjebak dalam optimum lokal (*local optima trap*)**: PSO adalah metaheuristik berbasis analogi kawanan fisik yang tidak memiliki model probabilitas data formal, sehingga rawan konvergensi prematur pada ruang hyperparameter campuran yang kontinu dan diskret.*
  > *3. **Ketiadaan mekanisme pruning**: PSO harus menjalankan seluruh iterasi meskipun konfigurasi partikel tersebut berkinerja buruk sejak awal.*
  >
  > *Oleh karena itu, kami beralih ke **Optuna dengan algoritma Tree-structured Parzen Estimator (TPE)** berbasis Bayesian Optimization. TPE memodelkan probabilitas bersyarat $P(x|y)$ secara cerdas dari trial-trial sebelumnya untuk mengarahkan pencarian ke kombinasi parameter paling menjanjikan. Selain itu, Optuna dilengkapi mekanisme automated pruning (seperti Median Pruner) yang secara otomatis menghentikan trial yang tidak berkinerja baik di tengah jalan, sehingga menghasilkan konvergensi yang jauh lebih cepat, hemat sumber daya, dan optimal secara global."*

---

### 3. Pertanyaan: Dataset memiliki ketidakseimbangan kelas ekstrem (1:16). Bagaimana Anda menjamin model tidak bias ke kelas mayoritas?
* **Rekomendasi Jawaban**:
  > *"Terima kasih atas pertanyaannya. Ketidakseimbangan kelas pada dataset acuan (685 klaim fraud vs 10.880 klaim normal) kami tangani melalui strategi bertingkat:*
  >
  > *Pada **level data**, kami menerapkan teknik resampling: mengombinasikan random under-sampling pada kelas mayoritas dan Synthetic Minority Over-sampling Technique (SMOTE) pada kelas minoritas fraud, sehingga ruang keputusan minoritas diperluas secara sintetis tanpa overfitting.*
  >
  > *Pada **level algoritma**, kami memanfaatkan hyperparameter `scale_pos_weight` pada LightGBM untuk memberikan penalti kerugian (*loss penalty*) yang lebih berat apabila model salah mengklasifikasikan klaim fraud.*
  >
  > *Pada **level evaluasi**, kami tidak menggunakan akurasi semu (*Accuracy*) sebagai patokan utama, melainkan berfokus pada **Recall, Precision, F1-Score, PR-AUC, dan minimalisasi Type II Error Rate** (False Negative Rate) untuk memastikan seluruh klaim fraud dapat dijaring semaksimal mungkin."*

---

### 4. Pertanyaan: Mengapa Anda secara khusus menekankan minimalisasi Type II Error (False Negative)?
* **Rekomendasi Jawaban**:
  > *"Terima kasih atas pertanyaannya. Dalam konteks industri asuransi, dampak kesalahan prediksi memiliki asimetri biaya yang sangat besar:*
  >
  > *Jika terjadi **Type I error (False Positive)**, sistem menandai klaim sah sebagai fraud, yang berakibat pada perlunya verifikasi dokumen tambahan oleh staf analis.*
  >
  > *Namun jika terjadi **Type II error (False Negative)**, sistem menandai klaim curang sebagai sah, sehingga klaim tersebut langsung dicairkan dan dibayarkan oleh perusahaan. Hal ini mengakibatkan kerugian finansial modal langsung, menggerus rasio underwriting, dan merusak stabilitas dana premi.*
  >
  > *Oleh karena itu, penelitian ini secara tegas memprioritaskan penurunan Type II error rate (klaim fraud yang lolos) ke tingkat yang lebih rendah dari capaian paper acuan (5,0%)."*

---

### 5. Pertanyaan: Bagaimana kontribusi penelitian ini dalam bidang Sistem Informasi, bukan hanya teknik komputer atau data science murni?
* **Rekomendasi Jawaban**:
  > *"Terima kasih atas pertanyaan kritis ini. Dalam bidang Sistem Informasi, fokus utama kita adalah **bagaimana teknologi informasi mendukung proses bisnis dan pengambilan keputusan manusia dalam organisasi**.*
  >
  > *Model ini dirancang sebagai **sistem pendukung keputusan (*decision support prototype*)** untuk tim penilai klaim (*claims adjusters*). Agar model dapat diadopsi secara manajerial dan mematuhi etika regulasi asuransi, kami mengintegrasikan metode **Explainable AI (TreeSHAP)**.*
  >
  > *Dengan TreeSHAP, model tidak beroperasi sebagai kotak hitam (*black-box*). Investigator klaim dapat melihat secara transparan fitur apa saja (misalnya besaran klaim, jenis kendaraan, pihak bersalah, usia pengemudi) yang berkontribusi positif atau negatif terhadap skor risiko klaim tersebut. Hal ini memberikan transparansi, akuntabilitas audit, dan rekomendasi yang dapat ditindaklanjuti secara langsung oleh manusia dalam alur operasional triase klaim asuransi."*
