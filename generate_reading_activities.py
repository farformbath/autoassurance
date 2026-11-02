import os
import docx
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def generate_final_reading_activities(template_path, out_docx, out_md):
    doc = Document(template_path)

    # 1. Update Title and Student Info in Header
    # Paragraph 0: Title
    doc.paragraphs[0].runs[0].text = ""
    doc.paragraphs[0].runs[1].text = "JURNAL AKTIVITAS MEMBACA JURNAL"

    # Paragraph 1: Nama
    doc.paragraphs[1].runs[3].text = "Irfan Fatkhurrizal"

    # Paragraph 2: NIM
    doc.paragraphs[2].runs[2].text = "\t2404140090"

    # 2. Update Signatures at Bottom
    doc.paragraphs[12].runs[13].text = "\tIrfan "
    doc.paragraphs[12].runs[14].text = "Fatkhurrizal"
    doc.paragraphs[13].runs[11].text = "\tNIM 2404140090"

    # 3. Articles Data (8 Verified Core Papers)
    articles = [
        {
            "tgl": "22/09/2026",
            "authors_year": "Wen, Y., Shen, Y., Liu, C., Zhang, Y., & Chen, F. (2023)",
            "title": "Voucher Abuse Detection with Prompt-based Fine-tuning on Graph Neural Networks",
            "pub": "Proceedings of the 32nd ACM International Conference on Information and Knowledge Management (CIKM '23)",
            "pages": ", pp. 4864–4870",
            "indexing": "Scopus / ACM Digital Library / CORE A",
            "doi": "https://doi.org/10.1145/3583780.3615505",
            "notes": [
                "Artikel ini meneliti pendeteksian penyalahgunaan voucher promosi pada platform e-commerce berskala besar menggunakan Graph Neural Networks (GNN) dengan pendekatan prompt-based fine-tuning (VPGNN). Penulis memodelkan interaksi antara pengguna, voucher, perangkat, dan alamat IP sebagai graf heterogen bipartit untuk mengatasi keterbatasan data latih berlabel kecurangan (skenario few-shot).",
                "Temuan penelitian membuktikan bahwa pemodelan graf sangat efektif membongkar sindikat akun terorganisir yang terhubung oleh kesamaan identitas jaringan. Namun, pendekatan ini memiliki kelemahan mendasar pada tingginya latensi komputasi inferensi graf yang mencapai hitungan detik hingga menit. Untuk kebutuhan layanan pesan-antar makanan instan, evaluasi saat pre-checkout menuntut respons sub-detik. Oleh karena itu, artikel ini menjadi rujukan celah riset yang sangat penting di Bab 1 dan Bab 2 untuk menunjukkan bahwa kebutuhan operasional harian memerlukan model tabular yang jauh lebih ringan dan cepat."
            ],
            "keywords": ["Voucher abuse,", "Graph Neural Networks,", "Prompt-based fine-tuning,", "Anomaly detection,", "E-commerce fraud,", "Few-shot learning"]
        },
        {
            "tgl": "24/09/2026",
            "authors_year": "Tian, Z., Liang, J., Huang, H., Wang, X., & Gao, M. (2024)",
            "title": "CATeye: Coupled Attribute-Topology Invariance Learning for Voucher Abuse Detection",
            "pub": "arXiv preprint arXiv:2409.07062",
            "pages": " (Diuji pada log industri Lazada)",
            "indexing": "Empirical Industry Case Study (Lazada)",
            "doi": "https://arxiv.org/abs/2409.07062",
            "notes": [
                "Penelitian ini menganalisis tantangan pergeseran pola penyerangan (distribution shift) dan taktik penyamaran sindikat pada penyalahgunaan voucher di platform e-commerce Lazada menggunakan kerangka kerja CATeye (Coupled Attribute-Topology Invariance Learning). Penulis memisahkan representasi fitur yang invarian dari atribut jaringan dan topologi graf yang kerap dimanipulasi oleh pelaku kecurangan terorganisir.",
                "Hasil pengujian pada data industri Lazada menunjukkan ketahanan model yang tinggi terhadap perubahan strategi penyerang lintas wilayah. Pelajaran penting dari paper ini bagi riset saya adalah pemahaman mengenai modus operandi manipulasi perangkat dan koneksi internet. Hal ini mendasari perancangan fitur tabular akselerasi transaksi (seperti frekuensi pesanan per subnet IP dan klaster perangkat) tanpa harus membangun infrastruktur basis data graf yang rumit."
            ],
            "keywords": ["Voucher abuse detection,", "Sybil detection,", "Invariance learning,", "Graph learning,", "Multi-accounting,", "Distribution shift"]
        },
        {
            "tgl": "26/09/2026",
            "authors_year": "Kumar, S., Gupta, R., Sharma, P., & Verma, A. (2024)",
            "title": "An intelligent approach to detect and predict online fraud transaction using XGBoost algorithm",
            "pub": "Indonesian Journal of Electrical Engineering and Computer Science (IJEECS)",
            "pages": ", 35(3), pp. 1491–1498",
            "indexing": "Scopus Q2 / SINTA 1 Equivalent",
            "doi": "https://doi.org/10.11591/ijeecs.v35.i3.pp1491-1498",
            "notes": [
                "Artikel ini menguji efektivitas algoritma Extreme Gradient Boosting (XGBoost) dalam mendeteksi anomali pada transaksi pembayaran digital terstruktur dibandingkan dengan Logistic Regression, Random Forest, dan K-NN. Eksperimen membuktikan bahwa XGBoost unggul secara konsisten dalam akurasi, stabilitas F1-score, serta kecepatan komputasi pada data tabular berdimensi tinggi.",
                "Keterbatasan utama paper ini terletak pada sifat keputusannya yang diperlakukan murni sebagai klasifikasi biner kaku (fraud vs normal) dengan ambang batas baku 0,5. Pendekatan biner ini sangat berisiko diterapkan pada program promosi akuisisi karena tingginya risiko salah blokir terhadap pengguna baru yang sah. Artikel ini saya jadikan rujukan empiris di Bab 2 untuk menjustifikasi pemilihan XGBoost pada data tabular, sekaligus memperkuat argumentasi bahwa luaran probabilitas model perlu dikonversi menjadi skor risiko bertingkat."
            ],
            "keywords": ["Online fraud detection,", "XGBoost classifier,", "Financial transactions,", "Machine learning,", "Anomaly detection,", "Tabular data"]
        },
        {
            "tgl": "29/09/2026",
            "authors_year": "Gupta, A., Shukla, S., Kikan, V., & Kumar, S. (2024)",
            "title": "Enhancing Fraud Detection in Credit Card Transactions using XGBoost and SMOTE: A Comparative Study",
            "pub": "2024 IEEE 4th International Conference on Smart Technologies for Power, Energy and Control (ICSPCRE)",
            "pages": ", pp. 1–6",
            "indexing": "IEEE Xplore / Scopus Indexed",
            "doi": "https://doi.org/10.1109/icspcre62303.2024.10675080",
            "notes": [
                "Penelitian ini membahas penanganan ketidakseimbangan kelas ekstrem pada deteksi kecurangan transaksi digital melalui integrasi algoritma XGBoost dan teknik penyeimbangan data SMOTE. Penulis mengevaluasi performa model menggunakan metrik kurva Precision-Recall (PR-AUC), Precision, dan Recall untuk menangkap kelas minoritas secara objektif.",
                "Hasil studi menunjukkan bahwa penanganan kelas minoritas mampu menekan angka false negative secara signifikan tanpa mengganggu stabilitas prediksi. Artikel ini menjadi pedoman penting bagi perancangan metodologi eksperimen di Bab 3, khususnya dalam membandingkan efektivitas pembobotan internal scale_pos_weight pada XGBoost terhadap teknik resampling sebelum probabilitas model dikalibrasi."
            ],
            "keywords": ["Fraud detection,", "XGBoost,", "SMOTE resampling,", "Class imbalance,", "Credit card transactions,", "PR-AUC evaluation"]
        },
        {
            "tgl": "02/10/2026",
            "authors_year": "Chen, T., & Guestrin, C. (2016)",
            "title": "XGBoost: A Scalable Tree Boosting System",
            "pub": "Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '16)",
            "pages": ", pp. 785–794",
            "indexing": "ACM SIGKDD / Scopus / CORE A* Flagship",
            "doi": "https://doi.org/10.1145/2939672.2939785",
            "notes": [
                "Sebagai makalah fondasi yang memperkenalkan sistem XGBoost, artikel ini menguraikan arsitektur komputasi gradient tree boosting berskala besar. Penulis merumuskan fungsi tujuan teratur yang meminimalkan kerugian logistik sekaligus membatasi kompleksitas struktur daun pohon untuk mencegah lewat-latih (overfitting).",
                "Keunggulan teknis yang paling relevan dengan riset saya adalah algoritma penanganan nilai kosong bawaan (sparsity-aware split finding). Fitur ini memungkinkan model tetap memproses data transaksi akun baru secara andal meskipun riwayat profil pengguna belum lengkap (kondisi cold-start). Formulasi matematis fungsi tujuan dan penalti daun dari paper ini menjadi landasan teoretis utama pada Bab 2."
            ],
            "keywords": ["XGBoost,", "Gradient tree boosting,", "Regularized learning,", "Sparsity-aware split,", "Scalable machine learning,", "Tabular data"]
        },
        {
            "tgl": "05/10/2026",
            "authors_year": "Lundberg, S. M., & Lee, S.-I. (2017)",
            "title": "A Unified Approach to Interpreting Model Predictions",
            "pub": "Advances in Neural Information Processing Systems (NeurIPS 2017)",
            "pages": ", Vol. 30, pp. 4765–4774",
            "indexing": "NeurIPS / CORE A* Flagship Conference",
            "doi": "https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html",
            "notes": [
                "Makalah ini merumuskan kerangka kerja terpadu Explainable AI melalui metode SHAP (SHapley Additive exPlanations) yang mengadaptasi konsep nilai Shapley dari teori permainan kooperatif. Algoritma TreeSHAP yang diusulkan mampu menghitung kontribusi marjinal setiap fitur pada model pohon keputusan secara efisien dalam waktu komputasi polinomial.",
                "Paper ini menjadi landasan penting untuk pilar People dalam perspektif Sistem Informasi pada Bab 2. Dengan mengintegrasikan TreeSHAP, model penilaian risiko yang dikembangkan tidak menjadi kotak hitam (black-box), melainkan menyediakan visualisasi atribusi fitur yang transparan sehingga analis risiko dapat memahami alasan spesifik di balik penentuan skor risiko pada setiap transaksi pengguna baru."
            ],
            "keywords": ["Explainable AI (XAI),", "SHAP,", "Shapley values,", "Model interpretability,", "Feature attribution,", "TreeSHAP"]
        },
        {
            "tgl": "08/10/2026",
            "authors_year": "Niculescu-Mizil, A., & Caruana, R. (2005)",
            "title": "Predicting Good Probabilities With Supervised Learning",
            "pub": "Proceedings of the 22nd International Conference on Machine Learning (ICML '05)",
            "pages": ", pp. 625–632",
            "indexing": "ACM ICML / Scopus / CORE A* Flagship",
            "doi": "https://doi.org/10.1145/1102351.1102430",
            "notes": [
                "Penelitian empiris ini mengevaluasi kualitas estimasi probabilitas dari berbagai algoritma pembelajaran mesin terawasi. Penulis membuktikan bahwa keluaran nilai margin dari algoritma boosted trees cenderung mengalami distorsi bentuk sigmoid dan tidak mencerminkan probabilitas frekuensi kejadian yang sebenarnya di dunia nyata.",
                "Penulis menunjukkan bahwa kalibrasi pasca-pelatihan, seperti Platt Scaling dan Isotonic Regression, terbukti secara signifikan menurunkan nilai Brier Score dan memulihkan keandalan probabilitas model. Artikel ini menjadi rujukan metodologis mutlak di Bab 2 dan Bab 3 untuk menjustifikasi bahwa probabilitas mentah XGBoost wajib dikalibrasi sebelum ditransformasikan menjadi indeks skor risiko kontinu berskala 0 hingga 100."
            ],
            "keywords": ["Probability calibration,", "Platt scaling,", "Isotonic regression,", "Boosted trees,", "Brier score,", "Supervised learning"]
        },
        {
            "tgl": "11/10/2026",
            "authors_year": "Fiarni, C., Gunawan, A. S., & Anthony, I. (2022)",
            "title": "Detection System of Promotion Abuse Using Similarity and Risk Scoring Methods",
            "pub": "Jurnal Nasional Teknik Elektro dan Teknologi Informasi (JNTETI)",
            "pages": ", 11(3), pp. 168–175",
            "indexing": "SINTA 2 Accredited National Journal",
            "doi": "https://doi.org/10.22146/jnteti.v11i3.3743",
            "notes": [
                "Penelitian nasional ini merancang sistem pendeteksi penyalahgunaan promosi pada e-commerce di Indonesia menggunakan analisis faktor eksploratori untuk mengidentifikasi 7 atribut transaksi penting, meliputi informasi jaringan, kontak, alamat, dan instrumen pembayaran. Penulis menerapkan algoritma kemiripan teks (Levenshtein distance) yang dipadukan dengan pembobotan skor risiko manual.",
                "Kelemahan pendekatan ini adalah ketergantungannya pada aturan pembobotan manual dan jarak kemiripan statis yang rentan dimanipulasi oleh variasi penulisan. Artikel ini sangat berharga sebagai acuan kontekstual lokal di Bab 1 dan Bab 3 dalam memetakan variabel atribut transaksi promosi yang relevan di Indonesia, yang pada penelitian saya dikembangkan lebih lanjut menggunakan model pembelajaran mesin adaptif."
            ],
            "keywords": ["Promotion abuse,", "Risk scoring,", "Similarity matching,", "E-commerce fraud,", "Account linkage,", "SINTA 2"]
        }
    ]

    # 4. Populate Table
    table = doc.tables[0]
    # Remove existing example rows from template
    while len(table.rows) > 1:
        table._tbl.remove(table.rows[-1]._tr)

    col_widths = [Cm(1.201), Cm(5.786), Cm(16.415), Cm(3.283)]

    for art in articles:
        row = table.add_row()
        for ci, w in enumerate(col_widths):
            row.cells[ci].width = w
            set_cell_margins(row.cells[ci])

        # Col 0: Tgl
        p0 = row.cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(art["tgl"])
        r0.font.name = "Calibri"
        r0.font.size = Pt(9)

        # Col 1: Reference
        p1 = row.cells[1].paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p1.paragraph_format.line_spacing = 1.15
        p1.paragraph_format.space_after = Pt(2)
        
        r_auth = p1.add_run(art["authors_year"] + ". ")
        r_auth.font.name = "Calibri"
        r_auth.font.size = Pt(9.5)
        
        r_title = p1.add_run(art["title"] + ". ")
        r_title.font.name = "Calibri"
        r_title.font.size = Pt(9.5)
        
        r_pub = p1.add_run(art["pub"])
        r_pub.font.name = "Calibri"
        r_pub.font.size = Pt(9.5)
        r_pub.italic = True
        
        r_pages = p1.add_run(art["pages"] + ".\n")
        r_pages.font.name = "Calibri"
        r_pages.font.size = Pt(9.5)
        
        r_idx = p1.add_run(f"Indexing: {art['indexing']}\n")
        r_idx.font.name = "Calibri"
        r_idx.font.size = Pt(8.5)
        r_idx.font.color.rgb = RGBColor(90, 90, 90)
        
        r_link = p1.add_run(f"Link: {art['doi']}")
        r_link.font.name = "Calibri"
        r_link.font.size = Pt(8.5)
        r_link.font.color.rgb = RGBColor(31, 78, 121)

        # Col 2: Notes (Catatan Penting Untuk Referensi Ke depan)
        c2 = row.cells[2]
        for p_idx, n_par in enumerate(art["notes"]):
            p_note = c2.paragraphs[0] if p_idx == 0 else c2.add_paragraph()
            p_note.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_note.paragraph_format.line_spacing = 1.15
            p_note.paragraph_format.space_after = Pt(4)
            r_note = p_note.add_run(n_par)
            r_note.font.name = "Calibri"
            r_note.font.size = Pt(9.5)

        # Col 3: Keywords
        c3 = row.cells[3]
        p_s = c3.paragraphs[0]
        p_s.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_s.paragraph_format.line_spacing = 1.05
        p_s.paragraph_format.space_after = Pt(2)
        r_s = p_s.add_run("[S]")
        r_s.font.name = "Calibri"
        r_s.font.size = Pt(9)
        
        for kw in art["keywords"]:
            p_kw = c3.add_paragraph()
            p_kw.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p_kw.paragraph_format.line_spacing = 1.05
            p_kw.paragraph_format.space_after = Pt(2)
            r_kw = p_kw.add_run(kw)
            r_kw.font.name = "Calibri"
            r_kw.font.size = Pt(8.5)

    # 5. Save DOCX
    doc.save(out_docx)
    print(f"Successfully generated DOCX matching template: {out_docx}")

    # 6. Generate Matching Markdown
    md_lines = [
        "**CONTOH JURNAL AKTIVITAS MEMBACA JURNAL**\n",
        "**Nama\t: \tIrfan Fatkhurrizal**  ",
        "**NIM\t:\t2404140090**\n",
        "| Tgl | Reference | Catatan Penting Untuk Referensi Ke depan | Keywords |",
        "| ----- | ----- | ----- | ----- |"
    ]
    for art in articles:
        ref_md = f"{art['authors_year']}. {art['title']}. *{art['pub']}*{art['pages']}. Indexing: {art['indexing']}. Link: {art['doi']}"
        notes_md = "  ".join(art["notes"])
        kw_md = "[S]<br>" + "<br>".join(art["keywords"])
        md_lines.append(f"| {art['tgl']} | {ref_md} | {notes_md} | {kw_md} |")

    md_lines.extend([
        "\nMengetahui  ",
        "Dosen Pengampu\t\t\t\t\t\t\t\t\t\t\t\tPenyusun Jurnal\n",
        "Zaenal Abidin, Ph.D\t\t\t\t\t\t\t\t\t\t\t\tIrfan Fatkhurrizal  ",
        "NIP 198204052005011001\t\t\t\t\t\t\t\t\t\t\tNIM 2404140090"
    ])

    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Successfully generated Markdown: {out_md}")

if __name__ == "__main__":
    tmpl = r"C:\projects\Promoabuse\references\Template Reading Activities.docx"
    target_docx = r"C:\projects\Promoabuse\Reading_Activities_XGBoost_Promotional_Abuse.docx"
    target_md = r"C:\projects\Promoabuse\Reading_Activities_XGBoost_Promotional_Abuse.md"
    generate_final_reading_activities(tmpl, target_docx, target_md)
