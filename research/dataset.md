# 3.2 Sumber dan Karakteristik Data

## 1. Sumber Data
Data yang digunakan dalam penelitian ini merupakan dataset sekunder transaksi klaim asuransi kendaraan bermotor (*automobile insurance claim fraud*) yang bersumber dari studi acuan Ding et al. (2025). Dataset ini merupakan integrasi data empiris dari lembaga investigasi fraud asuransi, data institusi perusahaan asuransi, serta repositori data terbuka internasional Kaggle/Oracle (*Automobile Insurance Claims Dataset*). Seluruh data telah melalui proses penyaringan untuk memastikan kelengkapan atribut dan mematuhi etika privasi tanpa mengekspos informasi pribadi yang dapat diidentifikasi (*Personally Identifiable Information* / PII).

## 2. Ukuran dan Distribusi Kelas (*Class Imbalance*)
Dataset ini memiliki total **11.565 baris data klaim**. Karakteristik distribusi variabel target biner `FraudFound_P` (di mana 1 merepresentasikan klaim fraudulent dan 0 merepresentasikan klaim sah/normal) disajikan pada tabel berikut:

| Kategori Label (`FraudFound_P`) | Jumlah Sampel | Persentase (%) | Status Kelas |
|---|---|---|---|
| `0` (Klaim Normal / Sah) | 10.880 | 94,08% | Kelas Mayoritas (*Majority Class*) |
| `1` (Klaim Fraud / Curang) | 685 | 5,92% | Kelas Minoritas (*Minority Class*) |
| **Total** | **11.565** | **100,00%** | **Rasio Ketidakseimbangan ~ 1 : 16** |

Tingginya disparitas antara kelas klaim normal dan klaim fraud (rasio 1:16) menunjukkan kondisi *extreme class imbalance*. Sebagaimana dikemukakan oleh Provost & Weiss (2011), model pembelajaran mesin yang dilatih langsung pada data terimbalans cenderung bias mengoptimalkan akurasi pada kelas mayoritas, sehingga menghasilkan tingkat kesalahan prediksi yang sangat tinggi pada kelas minoritas (*Type II error* / False Negative). Dalam domain industri asuransi, kegagalan mendeteksi klaim fraud membawa dampak finansial dan hukum yang jauh lebih merusak dibandingkan kesalahan deteksi pada klaim normal.

## 3. Atribut dan Fitur Variabel
Dataset mencakup 33 atribut fitur penjelas yang dikelompokkan ke dalam 5 (lima) dimensi operasional asuransi:

| No | Nama Variabel Fitur | Tipe Data | Deskripsi Operasional |
|---|---|---|---|
| 1 | `FraudFound_P` | Biner (0/1) | **Variabel Target**: 1 jika terbukti fraud, 0 jika klaim sah. |
| 2 | `ClaimSize` | Kontinu | Estimasi besaran nominal total pengajuan klaim biaya kerugian/perbaikan kendaraan. |
| 3 | `VehicleCategory` | Kategorikal | Klasifikasi tipe fisik kendaraan (misal: *Sedan*, *Sport*, *Utility/SUV*). |
| 4 | `VehiclePrice` | Ordinal | Rentang harga beli/nilai pasar kendaraan bermotor saat diasuransikan. |
| 5 | `Fault` | Biner/Kategori | Penentuan pihak yang bersalah dalam kecelakaan (*Policy Holder* atau *Third Party*). |
| 6 | `Age` | Kontinu | Usia pengemudi atau tertanggung utama pada saat insiden terjadi. |
| 7 | `Sex` | Kategorikal | Jenis kelamin tertanggung (*Male* / *Female*). |
| 8 | `MaritalStatus` | Kategorikal | Status pernikahan tertanggung (*Single*, *Married*, *Divorced*, *Widowed*). |
| 9 | `PolicyType` | Kategorikal | Paket pertanggungan polis asuransi (*All Risk*, *Total Loss Only / TLO*, *Third Party Liability*). |
| 10 | `Deductible` | Kontinu/Ordinal | Besaran nilai tanggungan sendiri yang wajib dibayar tertanggung sebelum klaim cair. |
| 11 | `PastNumberOfClaims` | Ordinal | Riwayat frekuensi klaim yang pernah diajukan tertanggung pada periode polis sebelumnya. |
| 12 | `AgeOfVehicle` | Ordinal | Usia pemakaian kendaraan bermotor terhitung sejak tahun perakitan. |
| 13 | `PoliceReportFiled` | Biner (Y/N) | Ketersediaan berkas laporan resmi dari pihak kepolisian atas kecelakaan. |
| 14 | `WitnessPresent` | Biner (Y/N) | Ketersediaan saksi mata independen di lokasi kejadian perkara. |
| 15 | `NumberOfCars` | Ordinal | Jumlah total unit kendaraan yang terlibat dalam tabrakan/insiden. |
| 16 | `Make` | Kategorikal | Pabrikan/merk kendaraan (misal: Toyota, Honda, Ford, Mazda, dll.). |
| 17 | `AccidentArea` | Kategorikal | Klasifikasi wilayah geografis tempat kejadian kecelakaan (*Urban* atau *Rural*). |
| 18 | `Days_Policy_Accident` | Ordinal | Rentang hari antara tanggal penerbitan polis dengan tanggal terjadinya kecelakaan. |
| 19 | `Days_Policy_Claim` | Ordinal | Rentang hari antara tanggal penerbitan polis dengan tanggal pelaporan klaim. |
| 20 | `AgentType` | Kategorikal | Saluran distribusi akuisisi polis (*Internal Agent* atau *External Broker*). |
| ... | *Atribut Pendukung Lainnya* | Beragam | Meliputi atribut kalender klaim (*Month*, *WeekOfMonth*, *DayOfWeek*), verifikasi dokumen, dll. |

## 4. Tahapan Pra-Pemrosesan Data (*Data Preprocessing*)
Proses persiapan data (*Data Preparation*) dilakukan secara sistematis melalui langkah-langkah berikut:
1. **Pembersihan Data (*Data Cleaning*) & Imputasi**: Pemeriksaan terhadap anomali data, duplikasi, dan penanganan nilai hilang (*missing values*). Untuk variabel numerik kontinu, imputasi dilakukan menggunakan nilai rata-rata (*mean*) atau median distribusi, sedangkan variabel kategorikal diimputasi menggunakan modus (*most frequent value*).
2. **Transformasi & Encoding Variabel**:
   * *Ordinal Encoding*: Diterapkan pada variabel bertingkat seperti `AgeOfVehicle`, `VehiclePrice`, dan `PastNumberOfClaims`.
   * *One-Hot Encoding*: Diterapkan pada variabel nominal murni tanpa urutan alami seperti `Make`, `PolicyType`, dan `MaritalStatus`.
   * *Binary Encoding*: Diterapkan pada variabel biner seperti `Sex` (0/1), `Fault` (0/1), `PoliceReportFiled` (0/1), dan `WitnessPresent` (0/1).
3. **Standarisasi Fitur (*Z-score Normalization*)**: Seluruh fitur numerik distandarisasi agar memiliki rata-rata $\mu = 0$ dan standar deviasi $\sigma = 1$:
   $$x^* = \frac{x - \mu}{\sigma}$$
   Transformasi ini memastikan tidak ada variabel dengan skala nominal besar (seperti `ClaimSize`) yang mendominasi perhitungan bobot gradien model.
4. **Pembagian Data (*Data Splitting*)**: Data dibagi menjadi **80% Training Set (9.252 data)** dan **20% Test Set (2.313 data)** secara *Stratified Random Sampling* untuk mempertahankan proporsi rasio kelas 1:16 pada kedua subset data.
