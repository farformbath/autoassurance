# Skripsi Asuransi: Deteksi Fraud Klaim Asuransi Kendaraan Bermotor (UNNES 2026)

Repositori penelitian skripsi Program Studi Sarjana Sistem Informasi, FMIPA Universitas Negeri Semarang:

> **Judul**: *Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna*  
> **Artikel Acuan Utama**: Ding, N., Ruan, X., Wang, H., & Liu, Y. (2025). Automobile insurance fraud detection based on PSO-XGBoost model and interpretable machine learning method. *Insurance Mathematics and Economics*, 120, 51–60. https://doi.org/10.1016/j.insmatheco.2024.11.006

---

## 🎯 Fokus & Urgensi Penelitian
* **Domain**: Fraud klaim asuransi kendaraan bermotor (*automobile insurance fraud*).
* **Masalah Bisnis**: Estimasi IAIS mencatat 20%–30% dari total klaim asuransi terindikasi fraud, mengakibatkan lonjakan kerugian finansial perusahaan dan tingginya tingkat *Type II error* (klaim curang lolos bayar) pada proses pemeriksaan manual.
* **Kritik Metodologis Terdahulu**: Model PSO-XGBoost pada paper acuan membutuhkan beban komputasi masif (5.000 trial partikel), rentan terjebak dalam *local optima*, dan XGBoost lambat memori pada data tabular besar.
* **Solusi yang Dikembangkan**:
  1. Klasifikasi menggunakan **LightGBM** yang hemat memori dan cepat berkat GOSS dan EFB.
  2. Penyetelan hyperparameter cerdas menggunakan **Optuna berbasis Bayesian TPE** dengan mekanisme *automated pruning*.
  3. Penanganan ketidakseimbangan kelas ekstrem (rasio 1:16; 685 fraud vs 10.880 normal) menggunakan kombinasi *resampling* (SMOTE / Random Resampling) dan *cost-sensitive weighting*.
  4. Analisis interpretabilitas transparan menggunakan **TreeSHAP** untuk mendukung pengambilan keputusan (*decision support*) tim penilai klaim.

---

## 📂 Struktur Repositori

```
skripshit-asuransi/
├── project_context.md                     # Ground truth, judul, fenomena, RQs, & batasan
├── research_constraints.md                # Pemetaan 11 arahan revisi Bimbingan 1
├── AGENTS.md                              # Master architecture, workflow & integrasi MCP
├── requirements.txt                       # Dependensi Python
├── LOGBOOK_BIMBINGAN.md                   # Catatan log bimbingan berkala
│
├── references/                            # Rujukan & template proposal
│   ├── Template-Proposal-Skripsi-2026.md  # Template proposal skripsi resmi UNNES 2026
│   ├── RPS-Metopen.md                     # Panduan kuliah metodologi penelitian SI UNNES
│   ├── skripsi_references.bib             # Database sitasi BibTeX standar APA Edisi ke-7
│   └── pdfs/                              # PDF paper acuan bereputasi (Ding et al., 2025)
│
├── skills/                                # Keahlian metodologis bertahap
│   ├── research-methodology/SKILL.md      # Tahap 1: Latar Belakang (tanpa gambar), Batasan, RQ, Manfaat
│   ├── literature-review/SKILL.md         # Tahap 2: Matriks Literatur, Kritik Hyperparameter, Gap & Novelty
│   ├── dataset-ml/SKILL.md                # Tahap 3: Dataset 11.565 klaim, LightGBM, Optuna TPE, TreeSHAP
│   └── proposal-reviewer/SKILL.md         # Tahap 4: Audit Naskah Lengkap Bab 1-3 & Template UNNES 2026
│
├── research/                              # Naskah dokumen penelitian
│   ├── problem.md                         # Subbab 1.1: Latar belakang deduktif (tanpa gambar)
│   ├── research-question.md               # Subbab 1.2 & 1.3: Batasan masalah & 3 RQ terukur
│   ├── literature-matrix.md               # Subbab 1.6 & 2.1: Matriks penelitian terdahulu (Tabel 1.1)
│   ├── research-gap.md                    # Subbab 1.6 & 2.4: Research gap & novelty statement
│   ├── dataset.md                         # Subbab 3.2: Spesifikasi data 11.565 baris & rekayasa fitur
│   ├── methodology.md                     # Subbab 3.3–3.5: Pipeline CRISP-DM, LightGBM, Optuna, & TreeSHAP
│   └── proposal.md                        # Naskah lengkap proposal skripsi (Bab 1, Bab 2, Bab 3)
│
├── data/                                  # Penyimpanan data lokal (raw & processed)
└── src/                                   # Skrip pipeline pemodelan & visualisasi
```

---

## 🛠️ Toolchain & Instalasi

```bash
# Pastikan menggunakan Python 3.11+
python -m venv .venv
source .venv/bin/activate  # atau .venv\Scripts\activate pada Windows

# Instalasi dependensi
pip install -r requirements.txt
```
