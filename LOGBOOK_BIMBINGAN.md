# LOGBOOK BIMBINGAN SKRIPSI

* **Nama Mahasiswa**: [Nama Lengkap]
* **NIM**: [NIM Mahasiswa]
* **Program Studi**: Sarjana Sistem Informasi, FMIPA Universitas Negeri Semarang
* **Dosen Pembimbing**: [Nama Dosen Pembimbing]
* **Judul Skripsi**: *Pengembangan Model Deteksi Fraud Klaim Asuransi Kendaraan Bermotor Berbasis LightGBM dengan Optimasi Hyperparameter Menggunakan Optuna*

---

## 📅 Riwayat Aktivitas Bimbingan

### Bimbingan 1
* **Tanggal**: 2026-11-01 / Sesi Konsultasi Pertama
* **Topik Pembahasan**: Pergeseran Topik Skripsi dan Penyesuaian Proposal Berdasarkan Artikel Acuan
* **Artikel Acuan Ditugaskan**: Ding, N., Ruan, X., Wang, H., & Liu, Y. (2025). Automobile insurance fraud detection based on PSO-XGBoost model and interpretable machine learning method. *Insurance Mathematics and Economics*, 120, 51–60. Elsevier.
* **Catatan Revisi & Arahan Pembimbing (`bimbingan 1.txt`)**:
  1. `lgbm`: Mengganti model utama menjadi LightGBM.
  2. `optuna lgbm`: Menggunakan Optuna untuk optimasi hyperparameter LightGBM (menggantikan PSO).
  3. `dataset dari paper acuan`: Menggunakan dataset sekunder dari paper acuan (11.565 data klaim asuransi mobil, rasio 1:16).
  4. `bab 1 sesuaikan`: Menyesuaikan seluruh narasi Bab 1 ke domain asuransi kendaraan bermotor dan LightGBM-Optuna.
  5. `lt bllkg gausah gambar`: Latar belakang tidak boleh menggunakan gambar atau diagram alur.
  6. `maslah Utama data penelitian terdahulu terkait metode yang digunakan terkait hypermpamareter`: Fokus masalah utama pada telaah kritis penelitian terdahulu mengenai metode yang digunakan, khususnya efisiensi dan konvergensi hyperparameter tuning (kelemahan PSO/manual vs Optuna TPE).
  7. `Batasan masahlah berupa point2`: Batasan masalah wajib disajikan dalam bentuk poin-poin terstruktur (*bullet points*).
  8. `diperjelas dataset yang digunakan tool yang digunakan"`: Memperjelas detail dataset 11.565 baris dan toolchain (Python, LightGBM, Optuna, Scikit-learn, SHAP).
  9. `rumusan maslaah 3 aja cukup disesuaikan lgbm nya`: Rumusan masalah dibatasi tepat 3 butir pertanyaan terukur.
  10. `manfaat dibuat 2`: Manfaat penelitian dibagi tepat 2 (Manfaat Teoretis dan Manfaat Praktis).
  11. `kebaharuan diuopdate, terkait ansurance`: Kebaruan penelitian diperbarui pada domain deteksi fraud asuransi kendaraan bermotor.
* **Tindak Lanjut & Status**:
  * [X] Setup repositori baru di `C:\projects\skripshit-asuransi`.
  * [X] Penyusunan `research_constraints.md` dan `project_context.md`.
  * [X] Pembuatan arsitektur agen dan konfigurasi skills (`research-methodology`, `literature-review`, `dataset-ml`, `proposal-reviewer`).
  * [X] Penyusunan naskah awal Bab 1 (`research/problem.md`, `research/research-question.md`, `research/literature-matrix.md`, `research/research-gap.md`).
  * [ ] Penyusunan naskah utuh proposal `research/proposal.md` untuk diajukan pada Bimbingan 2.
