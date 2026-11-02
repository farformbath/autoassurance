# AGENTS.md — Master Architecture, Workflow & MCP Orchestration

> **Proyek Skripsi**: Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna  
> **Program Studi**: Sarjana Sistem Informasi, FMIPA Universitas Negeri Semarang (UNNES)  
> **Panduan Utama**: [`project_context.md`](project_context.md) & [`research_constraints.md`](research_constraints.md)  
> **Paper Acuan**: Ding et al. (2025), *Automobile Insurance Fraud Detection Based on PSO-XGBoost Model and Interpretable Machine Learning Method*, Insurance Mathematics and Economics (Elsevier).

---

## 🎯 Peta Ekosistem Proyek

Proyek ini menggunakan arsitektur modular yang mengintegrasikan panduan institusional UNNES, keahlian metodologis bertahap (*skills*), dokumen penelitian terstruktur (*research/*), dataset lokal (*data/*), toolchain machine learning (*src/*), serta presentasi (*presentation/*):

```
skripshit-asuransi/
├── project_context.md                     # Ground truth, judul, fenomena, RQs, & batasan
├── research_constraints.md                # Pemetaan 11 poin revisi arahan dosen pembimbing
├── AGENTS.md                              # Master architecture, workflow & integrasi MCP
├── requirements.txt                       # Dependensi Python (LightGBM, Optuna, SHAP, dll.)
├── LOGBOOK_BIMBINGAN.md                   # Catatan log bimbingan skripsi terstruktur
├── README.md                              # Ringkasan proyek & status riset
├── generate_docx.py                       # Skrip generator naskah proposal Word (format resmi UNNES)
├── generate_reading_activities.py         # Skrip pengisi jurnal membaca artikel acuan (Word)
│
├── references/                            # Rujukan resmi & naskah acuan
│   ├── Template-Proposal-Skripsi-2026.md  # Template proposal skripsi resmi UNNES 2026
│   ├── RPS-Metopen.md                     # Panduan kurikulum metode penelitian SI UNNES
│   ├── Template Reading Activities.docx   # Template resmi logbook membaca artikel
│   ├── skripsi_references.bib             # Database sitasi BibTeX standar APA Edisi ke-7
│   └── pdfs/                              # PDF paper acuan bereputasi (Ding et al., 2025)
│
├── skills/                                # Keahlian metodologis lokal (Start to End)
│   ├── research-methodology/SKILL.md      # [START] Tahap 1: Latar Belakang (tanpa gambar), Batasan, RQ, Manfaat
│   ├── literature-review/SKILL.md         # [PHASE 2] Tahap 2: Matriks Literatur, Kritik Hyperparameter, Gap & Novelty
│   ├── dataset-ml/SKILL.md                # [PHASE 3] Tahap 3: Dataset 11.565 klaim, LightGBM, Optuna TPE, TreeSHAP
│   ├── proposal-reviewer/SKILL.md         # [END] Tahap 4: Audit Naskah Lengkap Bab 1-3 & Template UNNES 2026
│   └── bolt-slides/                       # [PRESENTASI] Slide deck interaktif seminar proposal (React + Vite)
│
├── research/                              # Modul dokumen naskah penelitian
│   ├── problem.md                         # Subbab 1.1: Latar belakang deduktif (tanpa gambar)
│   ├── research-question.md               # Subbab 1.2 & 1.3: Batasan masalah (poin) & 3 RQ terukur
│   ├── literature-matrix.md               # Subbab 1.6 & 2.1: Matriks penelitian terdahulu (Tabel 1.1)
│   ├── research-gap.md                    # Subbab 1.6 & 2.4: Research gap & novelty statement
│   ├── dataset.md                         # Subbab 3.1 & 3.2: Spesifikasi data 11.565 baris & rekayasa fitur
│   ├── methodology.md                     # Subbab 3.3–3.5: Pipeline CRISP-DM, LightGBM, Optuna, & TreeSHAP
│   └── proposal.md                        # Naskah lengkap proposal skripsi (Bab 1, Bab 2, Bab 3)
│
├── data/                                  # Penyimpanan data lokal
│   ├── raw/                               # Data mentah klaim asuransi (fraud_oracle / car claims)
│   └── processed/                         # Data hasil pembersihan, encoding, dan resampling
│
├── presentation/                          # Aplikasi slide deck interaktif seminar proposal (React + Vite)
│   ├── src/                               # Komponen slide, visual dashboard, & anotasi
│   └── index.html                         # Entry point presentasi
│
└── src/                                   # Skrip pipeline pemodelan & visualisasi
    ├── preprocess.py                      # Pembersihan data, imputasi, dan Z-score scaling
    ├── tune_optuna.py                     # Optimasi hyperparameter LightGBM via Optuna (TPE)
    ├── evaluate.py                        # Evaluasi komparatif model vs baseline & Type II error
    └── explain_shap.py                    # Analisis interpretabilitas global & lokal (TreeSHAP)
```

---

## 🚀 Alur Kerja Start-to-End (Sequential Workflow)

```mermaid
flowchart TD
    subgraph Tahap 1: Inisiasi [Start]
        S1[Skill: research-methodology] --> M1[research/problem.md]
        S1 --> M2[research/research-question.md]
    end

    subgraph Tahap 2: Literatur & Gap
        S2[Skill: literature-review] --> M3[research/literature-matrix.md]
        S2 --> M4[research/research-gap.md]
    end

    subgraph Tahap 3: Eksperimen Teknis
        S3[Skill: dataset-ml] --> D1[data/raw & data/processed]
        S3 --> E1[src/tune_optuna.py & evaluate.py]
        S3 --> M5[research/dataset.md]
        S3 --> M6[research/methodology.md]
    end

    subgraph Tahap 4: Penulisan & Audit [End]
        M1 & M2 & M3 & M4 & M5 & M6 --> P1[research/proposal.md]
        S4[Skill: proposal-reviewer] --> P1
        S5[Skill: academic-paper-reviewer] --> P1
        P1 --> OUT[Proposal Skripsi Final Siap Uji]
    end

    Tahap 1: Inisiasi --> Tahap 2: Literatur & Gap
    Tahap 2: Literatur & Gap --> Tahap 3: Eksperimen Teknis
    Tahap 3: Eksperimen Teknis --> Tahap 4: Penulisan & Audit
```

---

## 🛠️ Integrasi MCP Servers (Model Context Protocol)

Proyek ini mengaktifkan dan mengorkestrasi server MCP untuk mendukung akurasi dan integritas riset:

| MCP Server | Peran & Penggunaan Utama | Alat Utama |
|---|---|---|
| **`context7`** | Mengambil dokumentasi resmi dan sintaks API terkini untuk pustaka machine learning: sintaks LightGBM, konfigurasi studi Optuna (TPE Sampler & Median Pruner), Scikit-learn cross-validation, dan TreeSHAP visualizers. Mencegah halusinasi parameter usang. | `query-docs`, `resolve-library-id` |
| **`treg`** | Menelusuri metadata literatur ilmiah, mengecek DOI aktif, mengambil abstrak paper bereputasi di Scopus/IEEE/Elsevier, serta pengayaan data eksternal. | `treg_*` |
| **`ai_memory`** | Menyimpan memori persisten jangka panjang mengenai keputusan desain riset, catatan bimbingan dosen, serta checkpoint antar-sesi kerja agent. | `memory_query`, `memory_write_page`, `memory_briefing` |
| **`browser-harness`** | Otomasi browser jika diperlukan verifikasi repositori Kaggle, ScienceDirect, atau portal akademik resmi. | `browser_*` |

---

## 🎓 Integrasi Ekosistem Skill Akademik Global

Selain 5 skill lokal di atas, proyek ini mengintegrasikan seluruh kapabilitas dari katalog **Academic & Research Skills** global untuk menjamin kualitas standar publikasi internasional:

| Skill Akademik Global | Peran dalam Alur Skripsi | Tahap Eksekusi |
|---|---|---|
| **`academic-paper`** | Orkestrasi penulisan naskah akademis 12-agen berstandar jurnal internasional (Phase 0 Config s.d. Phase 7 Formatting). Digunakan saat menyusun naskah utuh Bab 1–3 atau konversi ke artikel publikasi. | Tahap 1, 2, 4 |
| **`academic-paper-reviewer`** | Simulasi *double-blind peer review* 5 sudut pandang: (1) Journal-Fit Reviewer, (2) Methodology Reviewer, (3) Domain Reviewer, (4) Perspective Reviewer, dan (5) Devil's Advocate Reviewer. Menghasilkan *Editorial Decision Letter* & *Revision Roadmap*. | Tahap 4 / Pre-submission |
| **`academic-pipeline`** | Meta-orkestrator pipeline riset menyeluruh yang menghubungkan riset, penulisan, review independen, hingga revisi. | Seluruh Tahap |
| **`deep-research` & `literature-search`** | Penelusuran sistematis literatur bereputasi (Elsevier, IEEE, Springer, ACM, Scopus) untuk ekstraksi matriks perbandingan dan validasi DOI. | Tahap 2 |
| **`novelty-assessment`** | Pengujian kebaruan ilmiah (*novelty test*) terhadap ruang solusi yang ada (PSO-XGBoost vs Optuna-LightGBM). | Tahap 2 |
| **`experiment-design`** | Desain eksperimen machine learning terstandarisasi: 5-fold stratified CV, ablation study, baseline bench, dan trade-off Type II error. | Tahap 3 |
| **`figure-generation` & `table-generation`** | Pembuatan grafik performa (ROC curve, PR curve, SHAP summary plot) dan tabel matriks format publikasi berbasis Matplotlib / Seaborn. | Tahap 3 |
| **`citation-management`** | Pemeliharaan database BibTeX (`references/skripsi_references.bib`) dan validasi kepatuhan format sitasi APA Edisi ke-7. | Tahap 2 & 4 |
| **`self-review`** | Audit mandiri naskah terhadap ketiadaan klaim tanpa bukti dan verifikasi FINER sebelum bimbingan dosen. | Tahap 4 |

---

## 📋 Panduan Eksekusi per Tahap

### 🟢 Tahap 1: Inisiasi & Formulasi Masalah (START)
* **Skill**: [`skills/research-methodology/SKILL.md`](skills/research-methodology/SKILL.md) & [`academic-paper`](~/.claude/skills/academic-paper)
* **Aturan Khusus Bimbingan 1**:
  * Subbab 1.1 Latar Belakang disusun deduktif **TANPA GAMBAR** (patuhi arahan: *lt bllkg gausah gambar*).
  * Masalah utama berakar pada kritik metode penelitian terdahulu: inefisiensi & risiko jebakan lokal optimasi hyperparameter (Grid Search / PSO) pada XGBoost, serta rasio klaim fraud yang tinggi (20-30%).
  * Subbab 1.2 Batasan Masalah disusun dalam **poin-poin (*bullet points*)**.
  * Subbab 1.3 Rumusan Masalah dibatasi tepat **3 Research Questions (RQ)** yang spesifik pada LightGBM, imbalance data, dan TreeSHAP.
  * Subbab 1.5 Manfaat Penelitian dibatasi tepat **2 poin** (Manfaat Teoretis dan Praktis).
* **Artefak**:
  * [`research/problem.md`](research/problem.md)
  * [`research/research-question.md`](research/research-question.md)

### 🟡 Tahap 2: Kajian Pustaka & Kebaruan
* **Skill**: [`skills/literature-review/SKILL.md`](skills/literature-review/SKILL.md), [`literature-search`](~/.claude/skills/literature-search), [`novelty-assessment`](~/.claude/skills/novelty-assessment)
* **Fokus**:
  * Menelaah minimal 7–10 artikel jurnal bereputasi (Elsevier, IEEE, Springer, ACM) terkait deteksi fraud asuransi, XGBoost, LightGBM, PSO, dan Bayesian Optimization (Optuna).
  * Membedah paper acuan Ding et al. (2025) secara mendalam: dataset 11.565 baris, rasio 1:16, akurasi PSO-XGBoost 95%, Type II error 5.0%, dan SHAP ranking.
  * Merumuskan *Research Gap* yang kokoh: Mengapa LightGBM + Optuna TPE lebih unggul dibanding PSO-XGBoost dalam kecepatan komputasi, penghindaran local optima, dan penurunan Type II error.
* **Artefak**:
  * [`research/literature-matrix.md`](research/literature-matrix.md) (Tabel 1.1)
  * [`research/research-gap.md`](research/research-gap.md)

### 🔵 Tahap 3: Dataset, Preprocessing, & Pemodelan LightGBM-Optuna
* **Skill**: [`skills/dataset-ml/SKILL.md`](skills/dataset-ml/SKILL.md), [`experiment-design`](~/.claude/skills/experiment-design), [`figure-generation`](~/.claude/skills/figure-generation)
* **Fokus**:
  * Integritas data mutlak: Dilarang keras mengarang angka metrik, label, atau dataset fiktif.
  * Penjelasan detail dataset: 11.565 baris klaim, 33 atribut, target `FraudFound_P`, rasio 1:16 imbalanced.
  * Penjelasan detail toolchain: Python 3.11+, LightGBM, Optuna, Scikit-learn, Imbalanced-learn, SHAP.
  * Pipeline CRISP-DM: Data Understanding, Preprocessing (Z-score, One-Hot/Ordinal Encoding), Resampling (SMOTE / Random Resampling), Optuna Hyperparameter Search (TPE), 5-Fold Stratified Cross-Validation, Baseline Benchmarking, dan TreeSHAP Explanation.
* **Artefak**:
  * [`research/dataset.md`](research/dataset.md)
  * [`research/methodology.md`](research/methodology.md)
  * Skrip implementasi di `src/`

### 🔴 Tahap 4: Penulisan Proposal & Audit Kepatuhan (END)
* **Skill**: [`skills/proposal-reviewer/SKILL.md`](skills/proposal-reviewer/SKILL.md), [`academic-paper-reviewer`](~/.claude/skills/academic-paper-reviewer), [`self-review`](~/.claude/skills/self-review)
* **Fokus**:
  * Menyatukan seluruh modul menjadi naskah utuh Bab 1, 2, dan 3 di [`research/proposal.md`](research/proposal.md).
  * Audit menyeluruh terhadap [`references/Template-Proposal-Skripsi-2026.md`](references/Template-Proposal-Skripsi-2026.md) dan [`research_constraints.md`](research_constraints.md).
  * Menjalankan simulasi peer-review 5-sudut pandang (termasuk Devil's Advocate) sebelum naskah diserahkan ke dosen pembimbing.
  * Menghasilkan dokumen Word resmi UNNES via `generate_docx.py`.

---

## 🛡️ Aturan Emas Kolaborasi (Master Directives)

1. **Anti-AI Slop**: Naskah harus bebas dari kata-kata klise generik (*"seamlessly"*, *"cutting-edge"*, *"pioneering"*, *"spearheaded"*). Setiap kalimat harus berupa fakta, keputusan arsitektur, bukti sitasi ilmiah, atau risiko metodologis.
2. **Kepatuhan Arahan Dosen Pembimbing**: 11 poin pada `research_constraints.md` bersifat mutlak. Jika terdapat kontradiksi, arahan dosen pembimbing selalu diprioritaskan.
3. **Prinsip Ponytail & YAGNI**: Default ke solusi paling sederhana, ringkas, dan langsung menjawab Research Questions tanpa pemborosan abstraksi.
4. **Reproducibility**: Seluruh hasil eksperimen, tabel perbandingan, dan grafik SHAP harus dapat direproduksi melalui kode Python di folder `src/`.
