# 3.3 Desain Penelitian dan Pipeline Pemodelan

Metodologi penelitian ini mengadopsi standar baku industri penambangan data **CRISP-DM (*Cross-Industry Standard Process for Data Mining*)** yang diselaraskan dengan kebutuhan pengembangan model pendukung keputusan (*decision support*) deteksi fraud asuransi kendaraan bermotor.

---

## 1. Tahapan Prosedur CRISP-DM

```mermaid
flowchart LR
    A[1. Business Understanding] --> B[2. Data Understanding]
    B --> C[3. Data Preparation]
    C --> D[4. Modeling: LightGBM + Optuna]
    D --> E[5. Evaluation: 5-Fold CV & Type II Error]
    E --> F[6. XAI: TreeSHAP Decision Support]
```

1. **Business Understanding**: Mengidentifikasi permasalahan bisnis tingginya kebocoran klaim fraud asuransi kendaraan (20%–30% dari total klaim), keterbatasan investigasi manual, serta perumusan tujuan pemodelan prediktif untuk meminimalkan *Type II error* (False Negative).
2. **Data Understanding**: Menganalisis karakteristik 11.565 data klaim dari studi acuan Ding et al. (2025), mendeteksi ketidakseimbangan kelas ekstrem (rasio 1:16), serta memeriksa korelasi antar-atribut fitur.
3. **Data Preparation**: Melakukan pembersihan data, penanganan nilai hilang, *ordinal/one-hot encoding*, standarisasi *Z-score*, dan penyeimbangan distribusi kelas menggunakan teknik *resampling* (*Random Under-Sampling* pada kelas mayoritas dan *SMOTE* pada kelas minoritas).
4. **Modeling**: Membangun model klasifikasi berbasis **LightGBM**, mengintegrasikan framework **Optuna** dengan algoritma *Tree-structured Parzen Estimator* (TPE) untuk optimasi hyperparameter otomatis, serta membangun model-model baseline sebagai pembanding (XGBoost standar, PSO-XGBoost, Random Forest, SVM).
5. **Evaluation**: Menguji performa model menggunakan *Stratified 5-Fold Cross-Validation* pada data uji (*test set*) 20% independen berdasarkan metrik *Recall*, *Precision*, *F1-Score*, *Type II error rate*, dan *ROC-AUC*.
6. **Deployment / Interpretability Prototype**: Menerapkan algoritma **TreeSHAP** untuk mengekstraksi nilai kontribusi fitur secara global dan lokal, memetakan interaksi fitur dominan, serta merancang rekomendasi alur triase klaim bagi investigator fraud.

---

## 2. Landasan Matematis Algoritma

### A. Algoritma Light Gradient Boosting Machine (LightGBM)
LightGBM merupakan penyempurnaan dari algoritma *Gradient Boosting Decision Tree* (GBDT) tradisional yang mengatasi keterbatasan komputasi pemindaian histogram penuh melalui dua teknik inti:

1. **Gradient-based One-Side Sampling (GOSS)**:
   Instans data dengan nilai gradien absolut besar memberikan kontribusi informasi perolehan (*information gain*) yang lebih tinggi. GOSS mempertahankan instans data dengan gradien $a\%$ teratas, dan mengambil sampel acak sebesar $b\%$ dari instans bergradien kecil. Perolehan informasi yang diestimasi $\tilde{V}_j(d)$ dihitung dengan mengalikan bobot $\frac{1-a}{b}$ pada sampel gradien kecil guna mengembalikan distribusi data asli tanpa bias:
   $$\tilde{V}_j(d) = \frac{1}{n} \left( \frac{(\sum_{x_i \in A_l} g_i + \frac{1-a}{b} \sum_{x_i \in B_l} g_i)^2}{n_l^j(d)} + \frac{(\sum_{x_i \in A_r} g_i + \frac{1-a}{b} \sum_{x_i \in B_r} g_i)^2}{n_r^j(d)} \right)$$

2. **Exclusive Feature Bundling (EFB)**:
   Pada data berdimensi tinggi, banyak fitur bersifat jarang (*sparse*) dan saling eksklusif (tidak pernah bernilai non-nol secara simultan). EFB mereduksi dimensi fitur dengan menggabungkan fitur-fitur eksklusif tersebut ke dalam satu bundel fitur terpadu (*single feature bundle*), sehingga memangkas kompleksitas pembentukan histogram dari $O(\text{data} \times \text{features})$ menjadi $O(\text{data} \times \text{bundles})$.

3. **Fungsi Objektif dan Regularisasi**:
   Fungsi objektif pada iterasi ke-$t$ meminimalkan fungsi kerugian logistik (*binary logloss*) ditambah suku regularisasi kompleksitas pohon:
   $$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
   di mana $g_i$ dan $h_i$ masing-masing adalah turunan pertama dan kedua dari fungsi loss, $T$ adalah jumlah daun, serta $\gamma$ dan $\lambda$ adalah parameter penalti regularisasi $L_1$ dan $L_2$.

---

### B. Optimasi Hyperparameter Berbasis Optuna (Tree-structured Parzen Estimator / TPE)
Framework Optuna menerapkan pendekatan *Sequential Model-Based Optimization* (SMBO) dengan algoritma TPE. Berbeda dengan regresi Gaussian Process standar yang memodelkan $P(y|x)$, TPE menerapkan teorema Bayes dengan memodelkan $P(x|y)$ secara non-parametrik:
$$P(x|y) = \begin{cases} \ell(x) & \text{jika } y < y^* \\ g(x) & \text{jika } y \ge y^* \end{cases}$$
di mana $y^*$ adalah nilai ambang batas (*quantile threshold*, biasanya persentil ke-15 atau ke-20 terbaik dari nilai fungsi objektif historis), $\ell(x)$ adalah estimasi densitas probabilitas untuk hyperparameter yang menghasilkan performa unggul, dan $g(x)$ adalah densitas untuk performa yang kurang memuaskan.

Akuisisi kandidat hyperparameter baru ditentukan dengan memaksimalkan *Expected Improvement* (EI):
$$EI_{y^*}(x) = \int_{-\infty}^{y^*} (y^* - y) P(y|x) dy = \frac{\gamma y^* \ell(x) - \ell(x) \int_{-\infty}^{y^*} P(y) dy}{\gamma \ell(x) + (1-\gamma) g(x)} \propto \left( \gamma + \frac{g(x)}{\ell(x)} (1-\gamma) \right)^{-1}$$
Dengan demikian, memaksimalkan EI ekuivalen dengan memaksimalkan rasio $\frac{\ell(x)}{g(x)}$, yang berarti Optuna memprioritaskan titik-titik hyperparameter yang memiliki peluang tinggi berada di kelas berkinerja terbaik $\ell(x)$ dan menjauhi kelas $g(x)$.

**Ruang Pencarian Hyperparameter LightGBM dalam Optuna**:
* `num_leaves`: `trial.suggest_int('num_leaves', 15, 255)`
* `max_depth`: `trial.suggest_int('max_depth', 3, 12)`
* `learning_rate`: `trial.suggest_float('learning_rate', 0.01, 0.3, log=True)`
* `n_estimators`: `trial.suggest_int('n_estimators', 50, 500)`
* `min_child_samples`: `trial.suggest_int('min_child_samples', 10, 100)`
* `subsample` (*bagging_fraction*): `trial.suggest_float('subsample', 0.5, 1.0)`
* `colsample_bytree` (*feature_fraction*): `trial.suggest_float('colsample_bytree', 0.5, 1.0)`
* `reg_alpha` ($L_1$): `trial.suggest_float('reg_alpha', 1e-8, 10.0, log=True)`
* `reg_lambda` ($L_2$): `trial.suggest_float('reg_lambda', 1e-8, 10.0, log=True)`
* `scale_pos_weight`: `trial.suggest_float('scale_pos_weight', 1.0, 16.0)`

---

### C. Interpretabilitas TreeSHAP
Untuk memastikan keterbukaan model (*model transparency*), digunakan algoritma TreeSHAP yang secara eksak menghitung nilai Shapley dari teori permainan kooperatif untuk ansambel pohon:
$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[ f_x(S \cup \{i\}) - f_x(S) \right]$$
di mana $F$ adalah himpunan seluruh fitur, $S$ adalah subset fitur tanpa fitur ke-$i$, dan $f_x(S)$ adalah ekspektasi bersyarat keluaran model dengan subset fitur $S$. TreeSHAP mengoptimalkan komputasi dari eksponensial $O(T L 2^{|F|})$ menjadi polinomial $O(T L D^2)$, di mana $T$ adalah jumlah pohon, $L$ jumlah daun maksimum, dan $D$ kedalaman pohon maksimum.

---

## 3. Metrik Evaluasi Kinerja & Formulasi Penurunan Type II Error

Model dievaluasi berdasarkan matriks konfusi (*confusion matrix*):

| Prediksi \ Aktual | Fraud Aktual (Positif = 1) | Normal Aktual (Negatif = 0) |
|---|---|---|
| **Prediksi Fraud (1)** | True Positive ($TP$) | False Positive ($FP$) (*Type I Error*) |
| **Prediksi Normal (0)** | False Negative ($FN$) (*Type II Error*) | True Negative ($TN$) |

1. **Akurasi**:
   $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
2. **Recall (Sensitivity)**:
   $$\text{Recall} = \frac{TP}{TP + FN}$$
3. **Precision**:
   $$\text{Precision} = \frac{TP}{TP + FP}$$
4. **Type II Error Rate (Tingkat Kegagalan Deteksi Fraud)**:
   $$\text{Type II Error Rate} = \frac{FN}{TP + FN} = 1 - \text{Recall}$$
   *Tujuan utama optimasi model adalah meminimalkan nilai Type II Error Rate serendah mungkin.*
5. **F1-Score**:
   $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
6. **Area Under Curve (ROC-AUC & PR-AUC)**: Mengukur kestabilan model di berbagai variasi ambang batas klasifikasi (*classification threshold*).

---

## 4. Spesifikasi Perangkat Lunak & Toolchain
* **Bahasa**: Python 3.11+
* **Framework Machine Learning**: LightGBM (v4.3+), XGBoost (v2.0+), Scikit-learn (v1.4+)
* **Framework Optimasi**: Optuna (v3.6+) dengan TPE Sampler dan Median Pruner
* **Interpretabilitas**: SHAP (v0.45+)
* **Penanganan Imbalance**: Imbalanced-learn (v0.12+)
* **Manipulasi & Visualisasi Data**: Pandas, NumPy, Matplotlib, Seaborn
