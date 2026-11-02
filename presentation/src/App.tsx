import Deck from './deck/Deck';
import Slide from './deck/Slide';
import Build from './deck/Build';
import Reveal from './deck/Reveal';
import Bento from './components/Bento';
import Split from './components/Split';
import CountUp from './components/CountUp';
import StatGrid from './components/StatGrid';
import Contrast from './components/Contrast';
import Steps from './components/Steps';
import Table from './components/Table';
import Tabs from './components/Tabs';
import Cover from './components/Cover';

export default function App() {
  return (
    <Deck>
      {/* ─────────────────────────────────────────────────────────────
          SLIDE 1: Judul, Identitas Peneliti & Afiliasi Akademik UNNES
          ───────────────────────────────────────────────────────────── */}
      <Cover
        nav="Judul & Identitas"
        notes="Ucapkan salam pembuka dan terima kasih kepada dewan penguji. Jelaskan secara lugas bahwa penelitian ini berfokus pada pengembangan model machine learning terapan untuk memitigasi kebocoran anggaran pemasaran pada platform food delivery, dengan studi kasus fenomena operasional pada GoFood."
        kicker="Seminar Proposal Skripsi · FMIPA Universitas Negeri Semarang"
        title={
          <>
            Model <span className="accent-text">Risk Scoring XGBoost</span> untuk
            Mitigasi Promotional Abuse
          </>
        }
        subtitle="Pengembangan Model Pembelajaran Mesin Probabilistik & Sistem Pendukung Keputusan pada Program Akuisisi Pengguna Baru Platform Food Delivery"
        foot="Sarjana Sistem Informasi · Jurusan Ilmu Komputer · UNNES 2026"
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 2: Fenomena Nyata, Urgensi Bisnis & Dampak Promo Abuse
          ───────────────────────────────────────────────────────────── */}
      <Split
        nav="Urgensi Masalah"
        notes="Tekankan bahwa masalah ini bukan fiksi, melainkan persoalan nyata bernilai miliaran rupiah yang dihadapi industri digital. 31% marketing budget bocor ke pengguna oportunistik multi-account."
        kicker="Urgensi Bisnis & Fenomena Nyata"
        title={
          <>
            Akun baru <span className="accent-text">belum tentu</span> pengguna baru.
          </>
        }
        body={
          <>
            <p>
              Persaingan ketat platform <em>food delivery</em> di Indonesia (seperti GoFood) mendorong program
              akuisisi pelanggan baru via voucher diskon agresif (50%–70%).
            </p>
            <p style={{ marginTop: 12 }}>
              Subsidi promosi bocor ke pelaku oportunistik <em>multi-accounting</em> /
              serangan <em>sybil</em>, menimbulkan kerugian finansial masif sekaligus
              mendistorsi metrik pertumbuhan (MAU &amp; CAC menjadi <em>vanity metrics</em>).
            </p>
          </>
        }
        media={
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16, width: '100%' }}>
            <div
              style={{
                background: 'var(--surface-2)',
                border: '1px solid var(--hair)',
                borderRadius: 'var(--radius)',
                padding: 'clamp(20px, 3vw, 28px)',
                boxShadow: 'var(--glow)',
              }}
            >
              <div className="kicker" style={{ color: 'var(--primary)' }}>
                Fakta Empiris Industri 2024
              </div>
              <div
                style={{
                  display: 'flex',
                  alignItems: 'baseline',
                  gap: 8,
                  margin: '12px 0 6px',
                }}
              >
                <span
                  className="figure accent-text"
                  style={{ fontSize: 'clamp(44px, 6vw, 68px)', fontWeight: 700 }}
                >
                  <CountUp to={31} suffix="%" />
                </span>
                <span className="lead" style={{ fontWeight: 600 }}>
                  Anggaran Pemasaran Bocor
                </span>
              </div>
              <p className="caption" style={{ color: 'var(--fg-muted)' }}>
                Rata-rata kerugian tahunan merchant digital akibat fraud promosi
                (DemandSage &amp; Riskified, 2024).
              </p>
            </div>

            <div
              style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
                gap: 12,
              }}
            >
              <div
                style={{
                  background: 'var(--surface)',
                  border: '1px solid var(--hair-2)',
                  borderRadius: 'var(--radius-sm)',
                  padding: 16,
                }}
              >
                <div className="kicker">Peringkat Ancaman</div>
                <div className="headline" style={{ fontSize: 24, margin: '6px 0 4px' }}>
                  Top 3
                </div>
                <div className="caption" style={{ color: 'var(--fg-muted)' }}>
                  Ancaman fraud digital utama industri (Ravelin Report, 2024).
                </div>
              </div>
              <div
                style={{
                  background: 'var(--surface)',
                  border: '1px solid var(--hair-2)',
                  borderRadius: 'var(--radius-sm)',
                  padding: 16,
                }}
              >
                <div className="kicker">Voucher Diskon</div>
                <div className="headline" style={{ fontSize: 24, margin: '6px 0 4px' }}>
                  50%–70%
                </div>
                <div className="caption" style={{ color: 'var(--fg-muted)' }}>
                  Subsidi akuisisi yang rentan dieksploitasi berulang kali.
                </div>
              </div>
            </div>
          </div>
        }
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 3: Keterbatasan Solusi Eksisting (Rule-Based Engine)
          ───────────────────────────────────────────────────────────── */}
      <Contrast
        nav="Keterbatasan Rule-Based"
        notes="Jelaskan bahwa pendekatan berbasis aturan statis telah mencapai titik jenuh dan membutuhkan pendekatan berbasis pembelajaran mesin probabilistik yang lebih adaptif."
        kicker="Evaluasi Solusi Eksisting"
        title="Mengapa Rule-Based Engine Mengalami Titik Jenuh?"
        left={{
          label: 'Mekanisme Eksisting',
          title: 'Static Rule-Based Engine',
          points: [
            'Aturan deterministik kaku: 1 Nomor Telepon = 1 Akun, 1 Device ID = 1 Voucher',
            'Mudah diakali sindikat via nomor virtual SMS OTP murah & aplikasi app cloner',
            'Keputusan biner kaku (Block vs Allow) tanpa memperhitungkan gradasi risiko',
            'Lonjakan False Positive: Pengguna baru sah ikut terblokir dan menimbulkan friksi',
          ],
        }}
        right={{
          label: 'Solusi Diusulkan',
          title: 'Adaptive Risk Scoring (XGBoost)',
          points: [
            'Evaluasi probabilistik adaptif berbasis pola non-linear fitur transaksi perdana',
            'Menghasilkan skor risiko kontinu (0–100) yang terkalibrasi secara matematis',
            'Mekanisme mitigasi bertingkat 3 zona: Auto-Approve, Step-Up OTP, Voucher Ineligible',
            'Menjaga kelancaran transaksi pengguna baru sah tanpa mengorbankan perlindungan anggaran',
          ],
        }}
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 4: Landasan 4 Pilar Sistem Informasi (Sosioteknis)
          ───────────────────────────────────────────────────────────── */}
      <Bento
        nav="Pilar Sistem Informasi"
        notes="Tunjukkan kepada penguji bahwa penelitian ini memenuhi kualifikasi keilmuan Sistem Informasi UNNES karena mengintegrasikan teknologi ke dalam proses bisnis dan organisasi."
        kicker="Landasan Keilmuan Sistem Informasi"
        title="Integrasi Empat Pilar Sosioteknis Sistem Informasi"
        tiles={[
          {
            c: 6,
            r: 1,
            k: 'Pilar 1 · Teknologi',
            title: 'Technology (Machine Learning)',
            body: 'Penerapan algoritma gradient boosted trees (XGBoost) untuk evaluasi risiko probabilistik berlatensi rendah (<50ms) pada alur pre-checkout transaksi pesanan.',
          },
          {
            c: 6,
            r: 1,
            k: 'Pilar 2 · Manusia',
            title: 'People (Customer & Risk Analyst)',
            body: 'Menjamin pengalaman mulus pelanggan baru yang sah tanpa friksi berlebih, sekaligus menyediakan interpretabilitas lokal TreeSHAP bagi analis risiko (fraud analyst).',
          },
          {
            c: 6,
            r: 1,
            k: 'Pilar 3 · Proses Bisnis',
            title: 'Process (Decision Support Workflow)',
            body: 'Mentransformasikan alur checkout konvensional menjadi mekanisme mitigasi proporsional 3 zona: Auto-Approve, Verifikasi Bertingkat (Step-Up), dan Pembatasan Voucher.',
          },
          {
            c: 6,
            r: 1,
            k: 'Pilar 4 · Organisasi',
            title: 'Organization (Governance & ROI)',
            body: 'Melindungi efektivitas alokasi anggaran pemasaran platform, mengeliminasi kebocoran subsidi promosi, serta menjamin validitas metrik pertumbuhan (MAU dan CAC).',
            variant: 'accent',
          },
        ]}
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 5: Rumusan Masalah & Research Questions (Provisional)
          ───────────────────────────────────────────────────────────── */}
      <Slide
        center
        nav="Research Questions"
        notes="Jelaskan bahwa RQ dirumuskan secara terukur dan metodologis untuk memandu tahapan penelitian. Provisional RQ bersifat adaptif terhadap validasi dataset riil."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 10 }}>
            Perumusan Masalah &amp; Panduan Metodologis
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              marginBottom: 'clamp(20px, 3vh, 32px)',
              maxWidth: '32ch',
            }}
          >
            Rumusan Masalah &amp; <span className="accent-text">Research Questions</span>
          </h2>
        </Reveal>

        <div style={{ width: '100%', maxWidth: 960, marginInline: 'auto' }}>
          <Tabs
            tabs={[
              {
                label: 'RQ1 · Sinyal & Fitur',
                content: (
                  <div
                    style={{
                      background: 'var(--surface)',
                      border: '1px solid var(--hair)',
                      borderRadius: 'var(--radius)',
                      padding: '24px 28px',
                      textAlign: 'left',
                    }}
                  >
                    <div className="kicker" style={{ color: 'var(--primary)' }}>
                      Research Question 1 (Fitur Transaksi Perdana)
                    </div>
                    <h3 className="headline" style={{ fontSize: 22, margin: '10px 0 12px' }}>
                      Karakteristik data transaksi dan sinyal perilaku apa yang paling
                      berkontribusi mengindikasikan risiko promotional abuse?
                    </h3>
                    <p className="lead" style={{ color: 'var(--fg-muted)', fontSize: 16 }}>
                      <strong>Fokus Analisis:</strong> Ekstraksi fitur <em>cold-start</em>{' '}
                      (ekonomi keranjang, atribut waktu, profil merchant) dan verifikasi kontribusi
                      prediktif menggunakan <em>TreeSHAP attribution values</em>.
                    </p>
                  </div>
                ),
              },
              {
                label: 'RQ2 · Efektivitas XGBoost',
                content: (
                  <div
                    style={{
                      background: 'var(--surface)',
                      border: '1px solid var(--hair)',
                      borderRadius: 'var(--radius)',
                      padding: '24px 28px',
                      textAlign: 'left',
                    }}
                  >
                    <div className="kicker" style={{ color: 'var(--primary)' }}>
                      Research Question 2 (Benchmark Model)
                    </div>
                    <h3 className="headline" style={{ fontSize: 22, margin: '10px 0 12px' }}>
                      Bagaimana efektivitas model XGBoost dibandingkan model baseline sederhana
                      pada data dengan ketidakseimbangan kelas ekstrem?
                    </h3>
                    <p className="lead" style={{ color: 'var(--fg-muted)', fontSize: 16 }}>
                      <strong>Fokus Analisis:</strong> Pengujian empiris metrik PR-AUC, Recall,
                      dan Precision terhadap Logistic Regression / Decision Tree di bawah skema
                      optimasi <em>scale_pos_weight</em>.
                    </p>
                  </div>
                ),
              },
              {
                label: 'RQ3 · Risk Scoring & DSS',
                content: (
                  <div
                    style={{
                      background: 'var(--surface)',
                      border: '1px solid var(--hair)',
                      borderRadius: 'var(--radius)',
                      padding: '24px 28px',
                      textAlign: 'left',
                    }}
                  >
                    <div className="kicker" style={{ color: 'var(--primary)' }}>
                      Research Question 3 (Decision Support System)
                    </div>
                    <h3 className="headline" style={{ fontSize: 22, margin: '10px 0 12px' }}>
                      Bagaimana mentransformasikan probabilitas prediksi menjadi skor risiko
                      bertingkat guna mendukung keputusan mitigasi proporsional?
                    </h3>
                    <p className="lead" style={{ color: 'var(--fg-muted)', fontSize: 16 }}>
                      <strong>Fokus Analisis:</strong> Kalibrasi probabilitas (Platt Scaling /
                      Isotonic Regression) ke skala 0–100 dan pemetaan ke 3 zona tindakan
                      operasional platform digital.
                    </p>
                  </div>
                ),
              },
            ]}
          />
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 6: Tinjauan Pustaka Primer, SOTA & 3 Celah Riset
          ───────────────────────────────────────────────────────────── */}
      <Bento
        nav="Literature & Gaps"
        notes="Soroti bahwa gap diturunkan dari sintesis literatur bereputasi internasional, bukan klaim subjektif. 7 studi primer terverifikasi menjadi landasan komparasi."
        kicker="Tinjauan Pustaka Primer &amp; Sintesis SOTA"
        title="Tiga Celah Riset Berbasis Bukti Literatur"
        tiles={[
          {
            c: 4,
            r: 1,
            k: 'Gap 1 · Komputasi Real-Time',
            title: 'Computational Latency Gap',
            body: 'Pendekatan Graph Neural Networks (Wen et al., 2023; Tian et al., 2024) efektif menangkap relasi kompleks tetapi memiliki latensi kueri tinggi. Platform food delivery memerlukan evaluasi sub-detik (<50ms) saat checkout.',
          },
          {
            c: 4,
            r: 1,
            k: 'Gap 2 · Granularitas Keputusan',
            title: 'Binary Decision Gap',
            body: 'Mayoritas literatur machine learning (Kumar et al., 2024; Gupta et al., 2024) berhenti pada klasifikasi biner kaku (fraud vs normal), tanpa merancang stratifikasi skor risiko bertingkat untuk mitigasi proporsional.',
          },
          {
            c: 4,
            r: 1,
            k: 'Gap 3 · Kendala Data Awal',
            title: 'New-User Cold-Start Gap',
            body: 'Ketiadaan riwayat transaksi masa lalu pada akun baru menuntut rekayasa fitur khusus dari transaksi perdana (basket economics, timing, merchant affinity) yang terbebas dari data leakage.',
            variant: 'accent',
          },
        ]}
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 7: Posisi Kebaruan Penelitian (Novelty Statement)
          ───────────────────────────────────────────────────────────── */}
      <Slide
        center
        nav="Novelty Statement"
        notes="Paparkan kebaruan dengan percaya diri tanpa klaim berlebihan. Tiga pilar kontribusi: Kontekstual, Metodologis, dan Sistem Informasi."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 12 }}>
            Pernyataan Kebaruan Ilmiah
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              maxWidth: '30ch',
              fontSize: 'clamp(28px, 4vw, 46px)',
              lineHeight: 1.25,
            }}
          >
            Posisi Kebaruan &amp; <span className="accent-text">Kontribusi Riset</span>
          </h2>
        </Reveal>

        <Reveal delay={0.12}>
          <div
            style={{
              background: 'var(--surface-2)',
              border: '1px solid var(--hair)',
              borderRadius: 'var(--radius)',
              padding: 'clamp(20px, 3vh, 32px) clamp(24px, 4vw, 44px)',
              maxWidth: 960,
              margin: '24px auto',
              boxShadow: 'var(--shadow)',
              textAlign: 'center',
            }}
          >
            <p
              className="lead"
              style={{
                fontSize: 'clamp(17px, 1.8vw, 22px)',
                fontStyle: 'italic',
                color: 'var(--fg)',
                lineHeight: 1.6,
              }}
            >
              “Pengembangan model <strong>risk scoring berbasis XGBoost</strong> pada data
              tabular transaksi perdana pengguna baru (<em>cold-start</em>) platform food delivery,
              dengan mentransformasikan probabilitas terkalibrasi menjadi skor risiko bertingkat
              (Low, Medium, High) yang dilengkapi interpretasi fitur SHAP guna mendukung keputusan
              mitigasi promosi yang proporsional.”
            </p>
          </div>
        </Reveal>

        <Reveal delay={0.22}>
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
              gap: 16,
              maxWidth: 960,
              marginInline: 'auto',
            }}
          >
            <div
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--hair-2)',
                borderRadius: 'var(--radius-sm)',
                padding: '16px 20px',
                textAlign: 'left',
              }}
            >
              <div className="kicker" style={{ color: 'var(--primary)' }}>
                Dimensi Kontekstual
              </div>
              <div className="subhead" style={{ fontSize: 16, marginTop: 4 }}>
                Solusi spesifik <em>first-order cold-start</em> pada industri pesan-antar makanan.
              </div>
            </div>
            <div
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--hair-2)',
                borderRadius: 'var(--radius-sm)',
                padding: '16px 20px',
                textAlign: 'left',
              }}
            >
              <div className="kicker" style={{ color: 'var(--primary)' }}>
                Dimensi Metodologis
              </div>
              <div className="subhead" style={{ fontSize: 16, marginTop: 4 }}>
                Integrasi XGBoost + Kalibrasi Probabilitas (Platt/Isotonic) + TreeSHAP XAI.
              </div>
            </div>
            <div
              style={{
                background: 'var(--surface)',
                border: '1px solid var(--hair-2)',
                borderRadius: 'var(--radius-sm)',
                padding: '16px 20px',
                textAlign: 'left',
              }}
            >
              <div className="kicker" style={{ color: 'var(--primary)' }}>
                Dimensi Sistem Informasi
              </div>
              <div className="subhead" style={{ fontSize: 16, marginTop: 4 }}>
                Kerangka kerja <em>Decision Support</em> operasional mitigasi risiko 3-zona.
              </div>
            </div>
          </div>
        </Reveal>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 8: Metodologi Penelitian & Prosedur CRISP-DM Adaptif
          ───────────────────────────────────────────────────────────── */}
      <Steps
        nav="Metodologi Penelitian"
        notes="Jelaskan bahwa penelitian mengikuti kaidah ilmiah yang ketat di mana pengembangan model penuh dilakukan pasca-proposal setelah akuisisi data fisik tervalidasi."
        kicker="Kerangka Prosedur Ilmiah"
        title="Tahapan Prosedur Penelitian Berbasis CRISP-DM Adaptif"
        items={[
          {
            title: '1. Pemahaman Bisnis & Data',
            body: 'Identifikasi fenomena abuse, formulasi provisional RQ, penelaahan 7 literatur primer, dan spesifikasi kontrak data.',
          },
          {
            title: '2. Persiapan Data & Isolasi Leakage',
            body: 'Pembersihan data, penguncian fitur pre-checkout, split temporal (70:15:15), dan feature engineering.',
          },
          {
            title: '3. Pemodelan & Benchmark',
            body: 'Pelatihan XGBoost vs Baseline (Logistic Regression / Decision Tree) dengan Stratified 5-Fold CV.',
          },
          {
            title: '4. Kalibrasi Skor & TreeSHAP',
            body: 'Kalibrasi probabilitas ke skala 0–100 via Platt Scaling / Isotonic Regression dan ekstraksi nilai SHAP.',
          },
          {
            title: '5. Evaluasi & Decision Support',
            body: 'Pengujian metrik PR-AUC, simulasi threshold 3 zona tindakan, dan perancangan prototipe dashboard.',
          },
        ]}
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 9: Objek Data, Unit Analisis & Aturan Kontingensi
          ───────────────────────────────────────────────────────────── */}
      <Split
        nav="Data & Kontingensi"
        notes="Tegaskan bahwa penelitian memiliki manajemen risiko metodologi yang jelas dan tidak akan memaksakan manipulasi label palsu. Aturan kontingensi tertulis rapi."
        kicker="Data Governance & Kepatuhan Etika"
        title={
          <>
            Objek Penelitian &amp;{' '}
            <span className="accent-text">Aturan Kontingensi</span>
          </>
        }
        body={
          <>
            <p>
              Unit analisis adalah transaksi pesanan perdana akun baru pada alur{' '}
              <em>pre-checkout</em> platform food delivery (mengacu alur operasional GoFood).
            </p>
            <p style={{ marginTop: 12 }}>
              Penelitian memegang komitmen ketat <strong>Zero PII</strong> (seluruh pengenal
              identitas di-hash) dan <strong>Zero Data Fabrication</strong> (label target tidak
              direkayasa sembarangan).
            </p>
          </>
        }
        media={
          <div style={{ width: '100%' }}>
            <Table
              columns={['Aspek Parameter', 'Ketentuan & Spesifikasi']}
              rows={[
                ['Unit Analisis', 'Transaksi pesanan pertama (first-order checkout)'],
                ['Sumber Data Utama', 'Log transaksi industri teranomalisasi (DS-CAND-03)'],
                ['Perlindungan Privasi', 'Zero PII (Pseudonimisasi token & atribut identitas)'],
                [
                  'Kontingensi Opsi A',
                  'Dataset benchmark transaksi terbuka terverifikasi (Kaggle/Open)',
                ],
                [
                  'Kontingensi Opsi B',
                  'Data sekunder fintech berlisensi akademik (Persetujuan Pembimbing)',
                ],
              ]}
              highlightCol={0}
              caption="Tabel Spesifikasi Tata Kelola Data & Skenario Kontingensi Riset"
            />
          </div>
        }
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 10: Pemodelan XGBoost, Evaluasi & Decision Support
          ───────────────────────────────────────────────────────────── */}
      <Split
        flip
        nav="Evaluasi & Decision Support"
        notes="Rangkum bagaimana seluruh rancangan teknis ini bermuara pada perlindungan anggaran promosi dan pengalaman pengguna sah. Tutup presentasi dan buka sesi tanya jawab."
        kicker="Solusi Terapan Sistem Informasi"
        title={
          <>
            Evaluasi Metrik &amp;{' '}
            <span className="accent-text">Decision Support Framework</span>
          </>
        }
        body={
          <>
            <p>
              Model dievaluasi menggunakan <strong>PR-AUC</strong> sebagai metrik utama yang kebal
              terhadap ketidakseimbangan kelas ekstrem, didukung Recall, Precision, dan Brier Score.
            </p>
            <p style={{ marginTop: 12 }}>
              Probabilitas terkalibrasi ditransformasikan menjadi skor risiko 0–100 dan dipetakan ke
              dalam 3 zona kebijakan mitigasi operasional secara otomatis.
            </p>
          </>
        }
        media={
          <div style={{ display: 'flex', flexDirection: 'column', gap: 14, width: '100%' }}>
            <div
              style={{
                background: 'rgba(16, 185, 129, 0.08)',
                border: '1px solid rgba(16, 185, 129, 0.3)',
                borderRadius: 'var(--radius-sm)',
                padding: '16px 20px',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ color: '#10b981', fontWeight: 700, fontSize: 16 }}>
                  🟢 Low Risk Zone (Skor 0–30)
                </span>
                <span className="kicker" style={{ color: '#10b981' }}>
                  Auto-Approve
                </span>
              </div>
              <p className="caption" style={{ color: 'var(--fg-muted)', marginTop: 6 }}>
                Voucher promosi langsung diterapkan secara otomatis. Pengguna menikmati transaksi
                tanpa friksi verifikasi tambahan.
              </p>
            </div>

            <div
              style={{
                background: 'rgba(245, 158, 11, 0.08)',
                border: '1px solid rgba(245, 158, 11, 0.3)',
                borderRadius: 'var(--radius-sm)',
                padding: '16px 20px',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ color: '#f59e0b', fontWeight: 700, fontSize: 16 }}>
                  🟡 Medium Risk Zone (Skor 31–70)
                </span>
                <span className="kicker" style={{ color: '#f59e0b' }}>
                  Step-Up Challenge
                </span>
              </div>
              <p className="caption" style={{ color: 'var(--fg-muted)', marginTop: 6 }}>
                Tantangan verifikasi tambahan (OTP WhatsApp / re-autentikasi SMS). Mencegah bot tanpa
                langsung memblokir pengguna sah.
              </p>
            </div>

            <div
              style={{
                background: 'rgba(239, 68, 68, 0.08)',
                border: '1px solid rgba(239, 68, 68, 0.3)',
                borderRadius: 'var(--radius-sm)',
                padding: '16px 20px',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ color: '#ef4444', fontWeight: 700, fontSize: 16 }}>
                  🔴 High Risk Zone (Skor 71–100)
                </span>
                <span className="kicker" style={{ color: '#ef4444' }}>
                  Voucher Ineligible
                </span>
              </div>
              <p className="caption" style={{ color: 'var(--fg-muted)', marginTop: 6 }}>
                Voucher promosi ditolak secara terhormat. Pengguna tetap dapat melanjutkan pesanan
                dengan tarif normal (meminimalkan churn transaksi).
              </p>
            </div>
          </div>
        }
      />
    </Deck>
  );
}
