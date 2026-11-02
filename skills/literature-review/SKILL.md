---
name: literature-review
description: Panduan tahap 2 penelitian untuk pencarian literatur bereputasi deteksi fraud asuransi, penyusunan matriks perbandingan Tabel 1.1 template UNNES, kritik mendalam terhadap penyetelan hyperparameter (PSO vs Bayesian Optuna), perumusan research gap, dan novelty statement berstandar APA 7th.
---

# Skill: Literature Review (Tahap 2: Kajian Pustaka & Research Gap)

Skill ini digunakan pada **Tahap 2** untuk memetakan penelitian terdahulu mengenai *automobile insurance fraud detection*, ensemble learning (XGBoost, LightGBM), optimasi hyperparameter (Grid Search, PSO, Bayesian Optuna), serta interpretabilitas model (SHAP).

---

## 🎯 Fokus Kritis Revisi Bimbingan 1
Mengacu pada [`research_constraints.md`](../../research_constraints.md) poin 6 & 11:
1. **Kritik Metode Terdahulu Terkait Hyperparameter**:
   * Penyetelan manual dan Grid Search membutuhkan waktu komputasi eksponensial dan sering melewatkan kombinasi optimal dalam ruang kontinu.
   * *Particle Swarm Optimization (PSO)* pada paper acuan Ding et al. (2025) memiliki kelemahan: rentan konvergensi prematur (*local optima trap*), membutuhkan ribuan iterasi partikel yang membebani memori, serta tidak memiliki mekanisme *early stopping/pruning* terhadap uji coba (*trial*) yang buruk.
   * **Optuna (TPE)**: Menggunakan pendekatan probabilistik Bayesian yang memodelkan $P(x|y)$ secara cerdas, mengarahkan pencarian ke wilayah parameter berprobabilitas tinggi dengan jumlah evaluasi jauh lebih sedikit, serta dilengkapi algoritma *pruning* (Asynchronous Successive Halving / Median Pruner).
2. **Kebaruan Domain Asuransi Kendaraan Bermotor**:
   * Memperbarui kebaruan pada perbandingan head-to-head efisiensi komputasi, penurunan Type II error rate, dan interpretabilitas TreeSHAP antara LightGBM-Optuna dengan PSO-XGBoost pada dataset acuan yang sama (11.565 klaim).

---

## 🔍 Protokol Penelusuran Literatur

### 1. Kata Kunci Pencarian (Search Queries)
Gunakan kata kunci spesifik berikut (manfaatkan MCP `treg` atau portal akademik Scopus/ScienceDirect/IEEE):
* `"automobile insurance fraud detection" AND "machine learning"`
* `"vehicle insurance claims fraud" AND ("XGBoost" OR "LightGBM")`
* `"hyperparameter optimization" AND ("Optuna" OR "TPE" OR "Bayesian") AND "fraud detection"`
* `"PSO-XGBoost" OR "particle swarm optimization" AND "insurance fraud"`
* `"imbalanced classification" AND "insurance claim fraud" AND ("Type II error" OR "Recall")`
* `"TreeSHAP" OR "explainable AI" AND "insurance fraud detection"`

### 2. Artikel Kunci Wajib Bedah
1. **Paper Acuan Utama**:
   * Ding, N., Ruan, X., Wang, H., & Liu, Y. (2025). Automobile insurance fraud detection based on PSO-XGBoost model and interpretable machine learning method. *Insurance Mathematics and Economics*, 120, 51–60. https://doi.org/10.1016/j.insmatheco.2024.11.006
2. **Fondasi LightGBM & Algoritma GOSS/EFB**:
   * Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., & Liu, T.-Y. (2017). LightGBM: A highly efficient gradient boosting decision tree. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30, 3146–3154.
3. **Fondasi Optuna & Bayesian TPE**:
   * Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019). Optuna: A next-generation hyperparameter optimization framework. *Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining*, 2623–2631. https://doi.org/10.1145/3292500.3330701
4. **Fondasi TreeSHAP & Interpretabilitas**:
   * Lundberg, S. M., Erion, G., Chen, H., DeGrave, A., Prutkin, J. M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., & Lee, S.-I. (2020). From local explanations to global understanding with explainable AI for trees. *Nature Machine Intelligence*, 2(1), 56–67. https://doi.org/10.1038/s42256-019-0138-9

---

## 📊 Matriks Literatur (`research/literature-matrix.md`)
Susun minimal 7–10 artikel dalam format baku Tabel 1.1 Template UNNES:

| No. | Peneliti & Tahun | Judul & Venue Publikasi | Dataset & Konteks | Metode yang Digunakan | Penanganan Imbalance & Tuning | Metrik & Hasil Utama | Keterbatasan / Research Gap |
|---|---|---|---|---|---|---|---|
| 1 | Ding et al. (2025) | Automobile insurance fraud detection based on PSO-XGBoost model... (*Ins. Math. Econ.*) | 11.565 data klaim asuransi mobil (Kaggle/Oracle) | PSO-XGBoost, SVM, RF, DT, BPNN | Random Under/Over Sampling; PSO (50 partikel, 100 iterasi) | Akurasi 95%, Precision 95.4%, Recall 95%, Type II error 5.0% | Waktu komputasi PSO tinggi, tidak ada pruning trial, XGBoost berat memori pada split besar |
| 2 | ... | ... | ... | ... | ... | ... | ... |

---

## 💡 Perumusan Research Gap (`research/research-gap.md`)
Sajikan analisis gap menggunakan 3 pilar:
1. **Gap Algoritma Klasifikasi (Efficiency & Scalability Gap)**: XGBoost menghitung histogram eksak yang memakan memori besar pada dataset dengan puluhan ribu baris. LightGBM dengan GOSS dan EFB menawarkan kecepatan latih lebih tinggi tanpa mereduksi akurasi.
2. **Gap Optimasi Hyperparameter (Search Strategy Gap)**: PSO adalah algoritma metaheuristik populasi yang tidak memperhitungkan distribusi bersyarat riwayat pengujian. Optuna Bayesian TPE memodelkan $l(x)$ dan $g(x)$ secara adaptif untuk menemukan parameter optimal dengan evaluasi yang jauh lebih sedikit dan waktu lebih singkat.
3. **Gap Evaluasi Keputusan Triase Klaim (Operational Decision Gap)**: Sebagian besar riset hanya berfokus pada akurasi global dan mengabaikan trade-off False Negative (Type II error) yang berakibat fatal pada kerugian finansial asuransi. Penelitian ini mengintegrasikan threshold tuning dan TreeSHAP untuk menyeimbangkan presisi dan recall operasional.

---

## ✅ Kriteria Verifikasi Tahap 2
- [ ] Matriks literatur memuat minimal 7 paper jurnal/prosiding internasional bereputasi (2020–2025).
- [ ] Paper acuan Ding et al. (2025) dibedah secara komparatif dan mendalam.
- [ ] Research gap menyoroti secara spesifik keterbatasan penyetelan hyperparameter dan efisiensi algoritma ensemble.
- [ ] Format sitasi mematuhi APA Edisi ke-7 dengan DOI aktif.
