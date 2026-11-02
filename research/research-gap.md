# 1.6 & 2.4 Research Gap dan Kebaruan Penelitian (Novelty)

## 1. Analisis Kesenjangan Penelitian (*Research Gap*)
Berdasarkan sintesis kritis terhadap literatur deteksi fraud asuransi kendaraan bermotor dan telaah mendalam terhadap artikel acuan utama Ding et al. (2025), diidentifikasi 3 (tiga) kesenjangan penelitian utama:

### A. Kesenjangan Efisiensi Arsitektur Model (*Algorithmic & Scalability Gap*)
Penelitian terdahulu yang mengandalkan algoritma *Extreme Gradient Boosting* (XGBoost) seperti pada Ding et al. (2025) berhasil membuktikan bahwa model *gradient boosting* memiliki akurasi superior dibanding model linier atau pohon tunggal. Namun, XGBoost memiliki kelemahan struktural mendasar: algoritma ini melakukan pemindaian nilai fitur secara penuh (*exact greedy algorithm*) pada setiap pembentukan daun pohon. Pada dataset tabular dengan dimensi tinggi dan puluhan ribu data klaim, kebutuhan komputasi dan alokasi memori melonjak secara kuadratik. Belum ada penelitian komparatif yang meneliti secara mendalam efisiensi dan keandalan arsitektur **LightGBM** (dengan teknik *Gradient-based One-Side Sampling* dan *Exclusive Feature Bundling*) pada dataset klaim asuransi terstandardisasi tersebut dalam menekan waktu komputasi tanpa mengorbankan akurasi klasifikasi kelas minoritas fraud.

### B. Kesenjangan Strategi Optimasi Hyperparameter (*Search Efficiency & Convergence Gap*)
Penyetelan hyperparameter model *gradient boosting* pada studi terdahulu memiliki dua kutub ekstrem yang kurang ideal:
1. Penyetelan manual / *Grid Search* yang tidak efisien dan rentan melewatkan kombinasi optimal dalam ruang pencarian kontinu.
2. Penyetelan metaheuristik seperti *Particle Swarm Optimization* (PSO) pada paper acuan Ding et al. (2025). Meskipun PSO mampu mencapai akurasi 95%, algoritma ini membutuhkan alokasi komputasi yang sangat mahal (50 partikel × 100 iterasi = 5.000 kali pelatihan ulang model). Lebih jauh, PSO tidak memiliki representasi probabilistik formal dari riwayat trial sebelumnya, sehingga rentan mengalami *premature convergence* (terjebak dalam optimum lokal) dan tidak dapat melakukan *pruning* dini terhadap uji coba parameter yang tidak prospektif.

Belum ditemukan penelitian deteksi fraud klaim asuransi yang memanfaatkan **Optuna berbasis Bayesian Optimization (Tree-structured Parzen Estimator / TPE)**. Optuna memodelkan distribusi probabilitas $P(x|y)$ secara cerdas untuk memandu eksplorasi hyperparameter LightGBM, sekaligus menerapkan *pruning* otomatis untuk memangkas waktu pencarian secara radikal.

### C. Kesenjangan Evaluasi Risiko Operasional (*Decision Support & Type II Error Gap*)
Banyak penelitian machine learning pada fraud asuransi hanya berfokus pada metrik akurasi global (*Accuracy*). Padahal pada kondisi *class imbalance* ekstrem (rasio 1:16), akurasi 94% dapat diperoleh secara trivial hanya dengan memprediksi seluruh klaim sebagai normal, namun model tersebut memiliki *Type II error* 100% (semua fraud lolos). Penelitian ini secara eksplisit memposisikan **minimalisasi Type II Error Rate** ($1 - \text{Recall}$) sebagai metrik keberhasilan utama, serta mengintegrasikan metode **TreeSHAP** (*global feature ranking*, *summary distribution plot*, dan *interaction dependence plot*) untuk memberikan wawasan operasional yang dapat ditindaklanjuti secara langsung oleh tim investigator klaim di industri asuransi.

---

## 2. Pernyataan Kebaruan (*Novelty Statement*)
Kebaruan (*novelty*) penelitian ini terletak pada:
1. **Pengembangan Kerangka Kerja Deteksi Fraud Terintegrasi**: Menggabungkan arsitektur *Light Gradient Boosting Machine* (LightGBM) dengan optimasi hyperparameter otomatis berbasis Bayesian TPE (Optuna) pada dataset sekunder terstandardisasi 11.565 klaim asuransi kendaraan bermotor terimbalans (rasio 1:16) dari studi acuan Ding et al. (2025).
2. **Keunggulan Efisiensi & Konvergensi**: Menggantikan pendekatan metaheuristik PSO pada penelitian acuan dengan Optuna Bayesian TPE dan *automated median pruning*, yang secara teoretis dan empiris menghasilkan kecepatan konvergensi lebih tinggi, kebutuhan iterasi evaluasi yang lebih hemat, serta terhindar dari jebakan optimum lokal.
3. **Fokus Minimalisasi Type II Error dan Transparansi XAI**: Mengoptimalkan fungsi loss dan threshold klasifikasi secara spesifik untuk meminimalkan *Type II error rate* (klaim fraud yang lolos bayar) ke tingkat yang lebih rendah dari baseline acuan (5,0%), disertai pembuktian transparansi keputusan penilai klaim melalui interpretabilitas TreeSHAP multi-level.
