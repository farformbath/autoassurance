import docx
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os
import re

def create_proposal_document(output_path):
    doc = docx.Document()
    fig_dir = r"C:\projects\Promoabuse\research\figures"

    # Set Margins to UNNES standard (Top 4.0cm, Left 4.0cm, Bottom 3.0cm, Right 3.0cm)
    for section in doc.sections:
        section.top_margin = Cm(4.0)
        section.left_margin = Cm(4.0)
        section.bottom_margin = Cm(3.0)
        section.right_margin = Cm(3.0)
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)

    # Base Normal Style
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(12)
    font_normal.color.rgb = RGBColor(0, 0, 0)
    style_normal.paragraph_format.line_spacing = 1.5
    style_normal.paragraph_format.space_after = Pt(6)
    style_normal.paragraph_format.space_before = Pt(0)
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


    # Heading 1 Style (Judul 1)
    h1 = doc.styles['Heading 1']
    h1.font.name = 'Times New Roman'
    h1.font.size = Pt(14)
    h1.font.bold = True
    h1.font.color.rgb = RGBColor(0, 0, 0)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(18)
    h1.paragraph_format.line_spacing = 1.0

    # Heading 2 Style (Judul 2)
    h2 = doc.styles['Heading 2']
    h2.font.name = 'Times New Roman'
    h2.font.size = Pt(12)
    h2.font.bold = True
    h2.font.color.rgb = RGBColor(0, 0, 0)
    h2.paragraph_format.space_before = Pt(14)
    h2.paragraph_format.space_after = Pt(6)
    h2.paragraph_format.line_spacing = 1.5

    # Heading 3 Style (Judul 3)
    h3 = doc.styles['Heading 3']
    h3.font.name = 'Times New Roman'
    h3.font.size = Pt(12)
    h3.font.bold = True
    h3.font.italic = True
    h3.font.color.rgb = RGBColor(0, 0, 0)
    h3.paragraph_format.space_before = Pt(10)
    h3.paragraph_format.space_after = Pt(4)
    h3.paragraph_format.line_spacing = 1.5
    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="B0B0B0", sz="4", val="single"):
        tblPr = table._tbl.tblPr
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr.append(borders)

    # Paragraph Builders
    def add_major_title(title_text):
        p = doc.add_paragraph(style='Heading 1')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(18)
        r = p.add_run(title_text.upper())
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        return p

    def add_chapter_title(bab_text, title_text):
        p = doc.add_paragraph(style='Heading 1')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(18)
        r = p.add_run(f"{bab_text.upper()}\n{title_text.upper()}")
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        return p

    def add_subheading(text):
        p = doc.add_paragraph(style='Heading 2')
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        r = p.add_run(text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        return p

    def add_subsubheading(text):
        p = doc.add_paragraph(style='Heading 3')
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.5
        r = p.add_run(text)
        r.bold = True
        r.italic = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        return p

    foreign_terms_list = [
        # Multi-word phrases & titles (longest first)
        r'Coupled Attribute-Topology Invariance Graph Learning',
        r'Coupled Attribute-Topology Invariance Learning',
        r'Voucher Abuse Detection with Prompt-based Fine-tuning on Graph Neural Networks',
        r'Voucher Abuse Detection with Prompt-based Fine-tuning',
        r'An intelligent approach to detect and predict online fraud transaction using XGBoost algorithm',
        r'Enhancing Fraud Detection in Credit Card Transactions using XGBoost and SMOTE: A Comparative Study',
        r'XGBoost: A Scalable Tree Boosting System',
        r'A Unified Approach to Interpreting Model Predictions',
        r'Predicting Good Probabilities With Supervised Learning',
        r'CATeye: Coupled Attribute-Topology Invariance Learning',
        r'Prompt-based Fine-tuning on Graph Neural Networks',
        r'Business Intelligence and Predictive Analytics',
        r'Design Science Research in Information Systems',
        r'Cross-Industry Standard Process for Data Mining',
        r'Zero Personally Identifiable Information',
        r'Personally Identifiable Information',
        r'Synthetic Minority Over-sampling Technique',
        r'binary decision: allow or block',
        r'Stratified 5-Fold Cross-Validation',
        r'orders_per_device_group_24h',
        r'address_cluster_frequency',
        r'orders_per_subnet_24h',
        r'multi-hop graph relationships',
        r'frictionless customer journey',
        r'production-grade anti-fraud engine',
        r'disposable virtual numbers',
        r'disposable virtual number',
        r'policy and promotional abuse',
        r'time-window boundary effect',
        r'time-window boundary',
        r'Time-Based Holdout Split',
        r'Key Performance Indicators',
        r'Customer Acquisition Cost',
        r'sparsity-aware split finding',
        r'regularized objective function',
        r'few-shot anomaly detection',
        r'online food delivery',
        r'Customer Lifetime Value',
        r'sybil multi-accounting',
        r'static rule-based engine',
        r'decision-support artifact',
        r'Sociotechnical Systems Theory',
        r'Pool Adjacent Violators',
        r'look-ahead data leakage',
        r'prediction cutoff point',
        r'risk-monitoring dashboard',
        r'Step-Up Verification',
        r'first-order incentives',
        r'first-order incentive',
        r'customer acquisition',
        r'promotional abuse',
        r'promotional leakage',
        r'incentive fraud',
        r'voucher abuse',
        r'policy abuse',
        r'two-sided market',
        r'existing users',
        r'existing user',
        r'virtual numbers',
        r'virtual number',
        r'app cloner',
        r'multi-accounting',
        r'Monthly Active Users',
        r'vanity metrics',
        r'vanity metric',
        r'rule-based engine',
        r'rule-based',
        r'binary decision',
        r'allow or block',
        r'False Positive Rate',
        r'False Positive',
        r'False Negative',
        r'True Positive',
        r'True Negative',
        r'risk scoring',
        r'risk-scoring',
        r'risk score',
        r'machine learning',
        r'sub-second latency',
        r'sub-second',
        r'pre-checkout',
        r'pre checkout',
        r'checkout gate',
        r'Explainable AI',
        r'Explainable Artificial Intelligence',
        r'decision support',
        r'decision-support',
        r'production-grade',
        r'pure defense focus',
        r'pure defense',
        r'reverse engineering',
        r'bypass KYC',
        r'evasion techniques',
        r'evasion technique',
        r'research questions',
        r'research question',
        r'class imbalance',
        r'imbalanced',
        r'feature importance',
        r'local attribution',
        r'Precision-Recall AUC',
        r'Precision-Recall',
        r'Precision Recall',
        r'Average Precision',
        r'Confusion Matrix',
        r'Auto-Approve',
        r'Promotion Denial',
        r'Business Intelligence',
        r'Predictive Analytics',
        r'gradient tree boosting',
        r'boosted trees',
        r'gradient boosting',
        r'Fraud vs Normal',
        r'Block vs Allow',
        r'Graph Neural Networks',
        r'Graph Neural Network',
        r'Graph Learning',
        r'cold-start',
        r'cold start',
        r'research gap',
        r'Sociotechnical Systems',
        r'objective function',
        r'sparsity-aware',
        r'sparsity awareness',
        r'Platt Scaling',
        r'Isotonic Regression',
        r'Brier Score',
        r'waterfall plot',
        r'summary plot',
        r'velocity features',
        r'velocity feature',
        r'time-window',
        r'time window',
        r'Design Science Research',
        r'Business Understanding',
        r'Data Understanding',
        r'Data Preparation',
        r'Deployment Scaffolding',
        r'Time-Based Split',
        r'time-based split',
        r'data leakage',
        r'random split',
        r'Random Under-Sampling',
        r'Under-Sampling',
        r'Over-sampling',
        r'early stopping',
        r'cost-benefit tradeoff',
        r'cost-benefit trade-off',
        r'cost-benefit',
        r'Zero Fabrication Policy',
        r'benchmark dataset',
        r'ground-truth',
        r'ground truth',
        r'supervised learning',
        r'ensemble tree',
        r'weighted logistic loss',
        r'logistic loss',
        r'cost-sensitive loss',
        r'cost-sensitive',
        r'scale_pos_weight',
        r'maximum likelihood',
        r'game theory',
        r'distribution shift',
        r'basket economics',
        r'post-processing',
        r'few-shot',
        r'SMS gateway',
        r'cryptographic hashing',
        r'one-way hash',
        r'account_age_seconds',
        r'time_since_install',
        r'order_total_amount',
        r'discount_amount',
        r'discount_ratio',
        r'is_min_spend_exact',
        r'is_promo_abuse',
        r'isFraud',
        r'learning_rate',
        r'max_depth',
        r'n_estimators',
        r'colsample_bytree',
        r'online transaction fraud',
        r'credit card transactions',
        r'credit card',
        r'e-commerce',
        r'on-demand',
        r'black-box',
        r'TreeSHAP',
        r'XGBoost',
        r'SHAP',
        r'Zero PII',
        r'food delivery',
        r'checkout',
        r'overfitting',
        r'tradeoff',
        r'trade-off',
        r'frictionless',
        r'friction',
        r'benchmark',
        r'leaves',
        r'voucher',
        r'fraud analyst',
        r'fraud',
        r'cloner',
        r'emulator',
        r'reset',
        r'holdout',
        r'cross-validation',
        r'hyperparameter',
        r'tuning',
        r'wireframe',
        r'mockup',
        r'dashboard',
        r'baseline',
        r'merchant',
        r'proxy',
        r'subnet',
        r'univariate',
        r'subsample',
        r'Recall',
        r'Precision',
        r'F1-Score',
        r'F1-score',
        r'Accuracy',
        r'sybil'
    ]
    foreign_terms_list = sorted(set(foreign_terms_list), key=lambda x: len(x), reverse=True)
    foreign_pattern = re.compile(r'\b(' + '|'.join(foreign_terms_list) + r')\b', re.IGNORECASE)

    def add_formatted_runs(paragraph, text, base_size=Pt(12), default_bold=False, default_italic=False):
        md_pattern = re.compile(r'(\*\*.*?\*\*|\*.*?\*)')
        raw_tokens = md_pattern.split(text)
        
        for token in raw_tokens:
            if not token:
                continue
            if token.startswith('**') and token.endswith('**') and len(token) >= 4:
                r = paragraph.add_run(token[2:-2])
                r.font.name = 'Times New Roman'
                r.font.size = base_size
                r.bold = True
                if default_italic:
                    r.italic = True
            elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
                r = paragraph.add_run(token[1:-1])
                r.font.name = 'Times New Roman'
                r.font.size = base_size
                if default_bold:
                    r.bold = True
                r.italic = True
            else:
                pos = 0
                for m in foreign_pattern.finditer(token):
                    s, e = m.span()
                    if s > pos:
                        r = paragraph.add_run(token[pos:s])
                        r.font.name = 'Times New Roman'
                        r.font.size = base_size
                        if default_bold:
                            r.bold = True
                        if default_italic:
                            r.italic = True
                    r = paragraph.add_run(token[s:e])
                    r.font.name = 'Times New Roman'
                    r.font.size = base_size
                    if default_bold:
                        r.bold = True
                    r.italic = True
                    pos = e
                if pos < len(token):
                    r = paragraph.add_run(token[pos:])
                    r.font.name = 'Times New Roman'
                    r.font.size = base_size
                    if default_bold:
                        r.bold = True
                    if default_italic:
                        r.italic = True
    def add_body_p(text, indent=True):
        p = doc.add_paragraph()
        if indent:
            p.paragraph_format.first_line_indent = Cm(1.0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_formatted_runs(p, text, base_size=Pt(12))
        return p

    def add_equation_box(eq_text):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.5)
        p.paragraph_format.right_indent = Cm(1.5)
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(eq_text)
        r.font.name = 'Cambria Math'
        r.font.size = Pt(11)
        r.bold = True
        return p

    def add_numbered_item(num_text, text):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.first_line_indent = Cm(-0.6)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r_num = p.add_run(num_text + " ")
        r_num.bold = True
        r_num.font.name = 'Times New Roman'
        r_num.font.size = Pt(12)
        add_formatted_runs(p, text, base_size=Pt(12))
        return p

    def add_figure(img_filename, caption_text, width_cm=14.0):
        img_path = os.path.join(fig_dir, img_filename)
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            run = p_img.add_run()
            run.add_picture(img_path, width=Cm(width_cm))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(10)
            p_cap.paragraph_format.line_spacing = 1.15
            add_formatted_runs(p_cap, caption_text, base_size=Pt(10.5), default_bold=False)
        else:
            print("WARNING: Image not found:", img_path)

    # ==================== COVER PAGE ====================
    p_cov_sp = doc.add_paragraph()
    p_cov_sp.paragraph_format.space_before = Pt(36)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.line_spacing = 1.15
    p_title.paragraph_format.space_after = Pt(36)
    r_title = p_title.add_run("PENGEMBANGAN MODEL RISK SCORING BERBASIS XGBOOST UNTUK MENDUKUNG MITIGASI PROMOTIONAL ABUSE PADA PROGRAM AKUISISI PENGGUNA BARU PLATFORM FOOD DELIVERY")
    r_title.bold = True
    r_title.font.size = Pt(14)

    p_prop = doc.add_paragraph()
    p_prop.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_prop.paragraph_format.line_spacing = 1.15
    p_prop.paragraph_format.space_after = Pt(6)
    r_prop = p_prop.add_run("PROPOSAL SKRIPSI")
    r_prop.bold = True
    r_prop.font.size = Pt(13)

    p_syarat = doc.add_paragraph()
    p_syarat.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_syarat.paragraph_format.line_spacing = 1.15
    p_syarat.paragraph_format.space_after = Pt(48)
    p_syarat.add_run("diajukan sebagai salah satu syarat untuk memperoleh gelar\nSarjana Komputer")

    p_oleh = doc.add_paragraph()
    p_oleh.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_oleh.paragraph_format.line_spacing = 1.15
    p_oleh.paragraph_format.space_after = Pt(4)
    p_oleh.add_run("oleh:")

    p_mhs = doc.add_paragraph()
    p_mhs.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_mhs.paragraph_format.line_spacing = 1.15
    p_mhs.paragraph_format.space_after = Pt(64)
    r_nama = p_mhs.add_run("Irfan Fatkhurrizal\n")
    r_nama.bold = True
    p_mhs.add_run("NIM. 2404140090")

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.line_spacing = 1.15
    p_inst.paragraph_format.space_before = Pt(36)
    r_inst1 = p_inst.add_run("PROGRAM STUDI SARJANA SISTEM INFORMASI\n")
    r_inst1.bold = True
    r_inst2 = p_inst.add_run("FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM\n")
    r_inst2.bold = True
    r_inst3 = p_inst.add_run("UNIVERSITAS NEGERI SEMARANG\n")
    r_inst3.bold = True
    r_inst4 = p_inst.add_run("2026")
    r_inst4.bold = True

    # ==================== HALAMAN PERSETUJUAN ====================
    doc.add_page_break()
    add_major_title("PERSETUJUAN PEMBIMBING")

    add_body_p("Proposal skripsi berjudul “Pengembangan Model Risk Scoring Berbasis XGBoost untuk Mendukung Mitigasi Promotional Abuse pada Program Akuisisi Pengguna Baru Platform Food Delivery” yang disusun oleh:", indent=False)

    tbl_bio = doc.add_table(rows=3, cols=3)
    tbl_bio.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_bio.autofit = False
    col_w = [Cm(3.5), Cm(0.5), Cm(11.0)]
    bio_data = [
        ("Nama Mahasiswa", ":", "Irfan Fatkhurrizal"),
        ("NIM", ":", "2404140090"),
        ("Program Studi / Jurusan", ":", "Sarjana Sistem Informasi / Ilmu Komputer, FMIPA UNNES")
    ]
    for row_idx, data in enumerate(bio_data):
        row = tbl_bio.rows[row_idx]
        for col_idx, text in enumerate(data):
            cell = row.cells[col_idx]
            cell.width = col_w[col_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.3
            p.paragraph_format.space_after = Pt(2)
            p.add_run(text)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    add_body_p("telah disetujui untuk diajukan ke Seminar Proposal Skripsi Program Studi Sarjana Sistem Informasi FMIPA Universitas Negeri Semarang.", indent=False)

    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(36)
    p_sig.paragraph_format.line_spacing = 1.15
    p_sig.paragraph_format.left_indent = Cm(8.0)
    p_sig.add_run("Semarang, 27 September 2026\n\n\n\n\n")
    r_dosen = p_sig.add_run("[Nama Dosen Pembimbing, Gelar]\n")
    r_dosen.bold = True
    p_sig.add_run("NIP. [NIP Dosen Pembimbing]")

    # ==================== DAFTAR ISI ====================
    doc.add_page_break()
    add_major_title("DAFTAR ISI")
    toc_items = [
        ("HALAMAN JUDUL", "i"),
        ("PERSETUJUAN PEMBIMBING", "ii"),
        ("DAFTAR ISI", "iii"),
        ("DAFTAR TABEL", "v"),
        ("DAFTAR GAMBAR", "vi"),
        ("BAB 1 PENDAHULUAN", "1"),
        ("   1.1 Latar Belakang", "1"),
        ("   1.2 Batasan Masalah", "4"),
        ("   1.3 Rumusan Masalah", "5"),
        ("   1.4 Tujuan Penelitian", "6"),
        ("   1.5 Manfaat Penelitian", "6"),
        ("   1.6 Kebaruan Penelitian dan Celah Riset", "7"),
        ("BAB 2 KAJIAN PUSTAKA", "11"),
        ("   2.1 Tinjauan Pustaka", "11"),
        ("   2.2 Landasan Teoretik", "13"),
        ("      2.2.1 Promotional Abuse dalam Ekosistem Food Delivery", "13"),
        ("      2.2.2 Perspektif Sistem Informasi dalam Tata Kelola Risiko Promosi", "13"),
        ("      2.2.3 Algoritma Extreme Gradient Boosting (XGBoost)", "15"),
        ("      2.2.4 Teori Kalibrasi Probabilitas", "17"),
        ("      2.2.5 Interpretabilitas Model Menggunakan TreeSHAP", "18"),
        ("      2.2.6 Analisis Kritis Keterbatasan Algoritma XGBoost pada Domain Fraud", "19"),
        ("   2.3 Kerangka Berpikir", "20"),
        ("BAB 3 METODE PENELITIAN", "22"),
        ("   3.1 Pendekatan, Jenis, dan Prosedur Penelitian", "22"),
        ("   3.2 Objek dan Sumber Data", "24"),
        ("   3.3 Variabel dan Definisi Operasional", "26"),
        ("   3.4 Desain Eksperimen dan Pemodelan XGBoost", "28"),
        ("   3.5 Evaluasi dan Rancangan Decision Support", "30"),
        ("   3.6 Jadwal Rencana Pelaksanaan Penelitian", "33"),
        ("   3.7 Etika Penelitian", "34"),
        ("DAFTAR PUSTAKA", "35")
    ]

    tbl_toc = doc.add_table(rows=len(toc_items), cols=2)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_toc.autofit = False
    for idx, (title, page) in enumerate(toc_items):
        row = tbl_toc.rows[idx]
        cell_l = row.cells[0]
        cell_r = row.cells[1]
        cell_l.width = Cm(13.5)
        cell_r.width = Cm(1.5)
        
        p_l = cell_l.paragraphs[0]
        p_l.paragraph_format.line_spacing = 1.15
        p_l.paragraph_format.space_after = Pt(2)
        r_l = p_l.add_run(title)
        if title.startswith("BAB") or title in ["HALAMAN JUDUL", "PERSETUJUAN PEMBIMBING", "DAFTAR ISI", "DAFTAR TABEL", "DAFTAR GAMBAR", "DAFTAR PUSTAKA"]:
            r_l.bold = True
            
        p_r = cell_r.paragraphs[0]
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_r.paragraph_format.line_spacing = 1.15
        p_r.paragraph_format.space_after = Pt(2)
        r_r = p_r.add_run(page)
        if title.startswith("BAB") or title in ["HALAMAN JUDUL", "PERSETUJUAN PEMBIMBING", "DAFTAR ISI", "DAFTAR TABEL", "DAFTAR GAMBAR", "DAFTAR PUSTAKA"]:
            r_r.bold = True
    # ==================== DAFTAR TABEL ====================
    doc.add_page_break()
    add_major_title("DAFTAR TABEL")

    daftar_tabel_items = [
        ("Tabel 1.1  Matriks Perbandingan Penelitian Terdahulu yang Mendasari", "8"),
        ("Tabel 3.1  Matriks Evaluasi Kelayakan Kandidat Dataset", "25"),
        ("Tabel 3.2  Definisi Operasional Variabel Penelitian dan Kelompok Fitur", "27"),
        ("Tabel 3.3  Kerangka Keputusan Mitigasi Berbasis Skor Risiko", "31"),
        ("Tabel 3.4  Jadwal Rencana Pelaksanaan Penelitian", "34")
    ]

    tbl_dt = doc.add_table(rows=len(daftar_tabel_items), cols=2)
    tbl_dt.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_dt.autofit = False
    for idx, (title, page) in enumerate(daftar_tabel_items):
        row = tbl_dt.rows[idx]
        cell_l = row.cells[0]
        cell_r = row.cells[1]
        cell_l.width = Cm(13.5)
        cell_r.width = Cm(1.5)
        
        p_l = cell_l.paragraphs[0]
        p_l.paragraph_format.line_spacing = 1.2
        p_l.paragraph_format.space_after = Pt(4)
        p_l.add_run(title)
        
        p_r = cell_r.paragraphs[0]
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_r.paragraph_format.line_spacing = 1.2
        p_r.paragraph_format.space_after = Pt(4)
        p_r.add_run(page)
    # ==================== DAFTAR GAMBAR ====================
    doc.add_page_break()
    add_major_title("DAFTAR GAMBAR")
    daftar_gambar_items = [
        ("Gambar 1.1  Perbandingan Alur Pengguna Baru Sah vs Sindikat Promotional Abuse", "3"),
        ("Gambar 2.1  Kerangka Sosioteknis Sistem Informasi dalam Tata Kelola Risiko Promosi", "14"),
        ("Gambar 2.2  Diagram Alur Kerangka Berpikir Penelitian", "21"),
        ("Gambar 3.1  Prosedur Penelitian Pengembangan Model Berbasis Adaptasi CRISP-DM", "23"),
        ("Gambar 3.2  Arsitektur Pipeline Rekayasa Fitur dan Pemodelan XGBoost", "29"),
        ("Gambar 3.3  Alur Triase Mitigasi Proporsional dan Desain Prototipe Decision Support", "32")
    ]

    tbl_dg = doc.add_table(rows=len(daftar_gambar_items), cols=2)
    tbl_dg.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_dg.autofit = False
    for idx, (title, page) in enumerate(daftar_gambar_items):
        row = tbl_dg.rows[idx]
        cell_l = row.cells[0]
        cell_r = row.cells[1]
        cell_l.width = Cm(13.5)
        cell_r.width = Cm(1.5)
        
        p_l = cell_l.paragraphs[0]
        p_l.paragraph_format.line_spacing = 1.2
        p_l.paragraph_format.space_after = Pt(4)
        p_l.add_run(title)
        
        p_r = cell_r.paragraphs[0]
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_r.paragraph_format.line_spacing = 1.2
        p_r.paragraph_format.space_after = Pt(4)
        p_r.add_run(page)

    # ==================== BAB 1 PENDAHULUAN ====================
    doc.add_page_break()
    add_chapter_title("BAB 1", "PENDAHULUAN")

    add_subheading("1.1 Latar Belakang")
    add_body_p("Layanan pesan-antar makanan digital beroperasi pada pasar dua sisi dengan persaingan antarplatform yang menuntut ekspansi basis konsumen secara berkesinambungan. Di Indonesia, dinamika ini tampak nyata pada platform seperti GoFood dari PT GoTo Gojek Tokopedia Tbk yang mengalokasikan anggaran besar untuk mendanai program akuisisi pengguna baru. Strategi akuisisi tersebut direalisasikan melalui instrumen subsidi promosi transaksi perdana, seperti pemotongan harga langsung hingga 70 persen dan subsidi biaya pengantaran. Alokasi subsidi ini bertumpu pada asumsi rasional bahwa insentif finansial pada pesanan pertama akan menurunkan hambatan coba-coba konsumen, sehingga terbentuk kebiasaan bertransaksi yang menghasilkan nilai masa hidup pelanggan yang melampaui biaya akuisisi awal.")
    
    add_body_p("Namun, efektivitas ekonomi dari program akuisisi tersebut terhambat oleh asimetri informasi pada proses pendaftaran identitas digital. Kemudahan registrasi akun secara daring membuka celah terjadinya perilaku oportunistik berupa promotional abuse atau penyalahgunaan promosi. Fenomena operasional yang konsisten terjadi di lapangan menunjukkan bahwa akun yang tercatat secara administratif sebagai akun baru belum tentu merepresentasikan individu konsumen yang benar-benar baru. Pengguna lama memanfaatkan ketersediaan nomor ponsel virtual sekali pakai, aplikasi pengganda identitas perangkat, hingga penghapusan memori aplikasi untuk mendaftarkan puluhan identitas akun tiruan melalui serangan sybil. Praktik ini bahkan meluas hingga ke jual-beli akun baru siap pakai yang telah dibekali voucher promo di berbagai media sosial. Transaksi berulang ini dilakukan semata-mata demi menguras voucher diskon perdana yang hak peruntukannya dibatasi secara khusus bagi konsumen baru organik. Kontras antara alur pendaftaran pengguna baru sah dan rekayasa identitas oleh sindikat eksploitasi multi-akun ini tampak nyata pada titik intervensi sistem sebelum pemesanan diselesaikan, seperti diilustrasikan pada Gambar 1.1.")

    # GAMBAR 1.1
    add_figure("gambar_1_1_alur_eksploitasi_sybil.png", "Gambar 1.1  Perbandingan Alur Pengguna Baru Sah vs Sindikat Promotional Abuse", width_cm=14.5)

    add_body_p("Eksploitasi multi-akun tersebut menimbulkan dampak kerugian berlapis pada ekosistem platform. Pada aspek finansial, terjadi kebocoran subsidi promosi dalam jumlah besar. Laporan riset pencegahan kecurangan digital global mencatat bahwa penyalahgunaan promosi dan kebijakan menempati jajaran tiga besar ancaman operasional, dengan rata-rata potensi kebocoran mencapai 31 persen dari total anggaran pemasaran tahunan (DemandSage & Riskified, 2024; Ravelin, 2024). Di samping kerugian kas, fenomena ini mendistorsi indikator kinerja bisnis utama. Pembuatan akun tiruan memicu pembengkakan semu pada metrik pengguna aktif bulanan MAU dan biaya akuisisi pelanggan CAC. Akibatnya, manajemen menerima sinyal pertumbuhan yang bias, yang berisiko menyesatkan perencanaan kapasitas operasional dan alokasi investasi. Pada saat yang sama, hak calon konsumen baru yang sah terampas karena kuota promosi harian cepat habis terserap oleh akun tiruan, sementara mitra resto ikut dirugikan oleh fluktuasi pesanan manipulatif dengan nilai keranjang belanja yang ditekan seminimal mungkin.")

    add_body_p("Hingga saat ini, pertahanan yang diandalkan platform masih bertumpu pada mesin penyaring berbasis aturan statis. Pendekatan ini bekerja dengan mengevaluasi kondisi tunggal secara deterministik, seperti membatasi satu nomor telepon atau satu nomor identitas perangkat untuk satu kali klaim promo. Pendekatan statis memiliki kelemahan mendasar karena mudah ditembus melalui pergantian nomor virtual dan manipulasi parameter perangkat lunak. Kelemahan yang lebih kritis terletak pada sifat keputusannya yang biner kaku, yaitu hanya mengizinkan atau memblokir transaksi secara mutlak. Ketika aturan diperketat untuk menekan kecurangan, angka salah blokir meningkat drastis. Konsumen baru yang sah, seperti anggota keluarga dalam satu jaringan internet rumah atau penghuni asrama yang sama, ikut terblokir dari hak promosi mereka. Gesekan transaksi ini memicu pembatalan pesanan dan merusak kepercayaan pengguna pada transaksi pertama.")

    add_body_p("Kelemahan pendekatan aturan statis tersebut menunjukkan adanya celah penelitian yang nyata. Penelitian terdahulu di bidang kecurangan promosi sebagian besar terbagi ke dalam dua kutub ekstrem: pendekatan aturan biner yang kaku dengan angka salah blokir tinggi, atau pendekatan graf relasional graph neural networks yang memerlukan komputasi memori besar dan waktu inferensi lambat sehingga tidak memadai untuk evaluasi transaksi instan. Belum tersedia pendekatan yang menjembatani kebutuhan mitigasi risiko dengan kelancaran transaksi bisnis pada alur peninjauan pesanan pre-checkout. Untuk mengisi celah tersebut, diperlukan pendekatan penilaian risiko risk scoring berbasis analitik data prediktif. Penilaian risiko ini merupakan metode evaluasi kuantitatif yang mengkalkulasi probabilitas risiko suatu transaksi secara adaptif berdasarkan pola atribut historis, kemudian memetakannya ke dalam indeks skor kontinu bertingkat, mulai dari risiko rendah, sedang, hingga tinggi. Dengan pendekatan penilaian risiko, sistem pendukung keputusan dapat menerapkan mitigasi yang proporsional: meloloskan transaksi berisiko rendah tanpa hambatan, memberikan verifikasi tambahan pada risiko sedang, dan membatasi voucher hanya pada transaksi berisiko tinggi. Pendekatan ini memutus motif ekonomi eksploitasi multi-akun sekaligus melindungi kenyamanan bertransaksi pelanggan baru yang sah.")

    add_subheading("1.2 Batasan Masalah")
    add_body_p("Ruang lingkup penelitian ini difokuskan pada analisis transaksi pemesanan perdana akun baru pada platform layanan pesan-antar makanan digital dengan memanfaatkan atribut data tabular terstruktur pada titik evaluasi sebelum pembayaran pesanan dikonfirmasi pada tahap pre-checkout. Karakteristik alur bisnis, mekanisme insentif promosi perdana, dan rekayasa fitur dalam penelitian ini merujuk secara empiris pada fenomena operasional ekosistem GoFood di Indonesia sebagai kasus representatif industri, tanpa memerlukan intervensi langsung terhadap infrastruktur server produksi internal Gojek. Pengujian performa komputasi ditujukan pada pengembangan dan evaluasi model prediktif berbasis algoritma XGBoost yang kinerjanya dibandingkan secara objektif terhadap model pembanding linier logistic regression dan pohon keputusan decision tree. Luaran penelitian diposisikan secara tegas sebagai instrumen pendukung keputusan yang mentransformasikan probabilitas posterior terkalibrasi menjadi indeks skor risiko bertingkat beserta skenario mitigasi proporsional, bukan pembangunan mesin pertahanan otomatis kelas produksi skala penuh.")
    
    add_body_p("Dalam aspek tata kelola etika akademik dan kepatuhan hukum, penelitian ini memegang prinsip orientasi pertahanan murni. Penelitian ini tidak mencakup pengujian penetrasi, rekayasa balik, eksploitasi celah antarmuka pemrograman aplikasi, maupun teknik pemintasan protokol verifikasi identitas. Penelitian juga tidak menyediakan dokumentasi maupun instruksi prosedural yang dapat dimanfaatkan untuk melakukan kecurangan atau menghindari deteksi sistem. Seluruh atribut data yang dianalisis tunduk pada prinsip perlindungan privasi mutlak tanpa menggunakan informasi identitas pribadi Zero PII, dengan setiap indikator pengenal disamarkan melalui fungsi pengacakan satu arah sebelum proses pemodelan dilakukan.")

    add_subheading("1.3 Rumusan Masalah")
    add_body_p("Program akuisisi pengguna baru pada platform pesan-antar makanan mengalami inefisiensi alokasi anggaran promosi akibat eksploitasi pembuatan akun tiruan oleh pengguna lama. Pendekatan deteksi berbasis aturan statis terbukti tidak memadai karena rapuh terhadap manipulasi perangkat lunak dan menghasilkan angka salah blokir yang tinggi pada pelanggan sah akibat sifat vonisnya yang biner kaku. Diperlukan suatu model penilaian risiko prediktif berbasis XGBoost yang mampu mengevaluasi pola anomali data tabular transaksi perdana secara probabilistik, cepat, dan terkalibrasi guna mendukung pengambilan keputusan mitigasi yang proporsional.")
    
    add_body_p("Berdasarkan latar belakang dan rumusan masalah tersebut, pertanyaan penelitian dirumuskan sebagai berikut.", indent=False)
    add_numbered_item("1.", "Karakteristik fitur data transaksi perdana dan perilaku akun baru apa saja yang memberikan kontribusi atribusi paling signifikan dalam mengindikasikan risiko penyalahgunaan promosi pada platform pesan-antar makanan?")
    add_numbered_item("2.", "Bagaimana kinerja prediktif dan efisiensi komputasi model risk scoring berbasis XGBoost dibandingkan dengan model pembanding sederhana pada kondisi distribusi data transaksi yang mengalami ketidakseimbangan kelas ekstrem?")
    add_numbered_item("3.", "Bagaimana luaran probabilitas dari model XGBoost dapat dikalibrasi dan dipetakan secara matematis ke dalam indeks skor risiko bertingkat guna memandu skenario mitigasi operasional yang proporsional pada sistem pendukung keputusan?")

    add_subheading("1.4 Tujuan Penelitian")
    add_body_p("Sejalan dengan pertanyaan penelitian yang telah dirumuskan, tujuan yang hendak dicapai dalam penelitian ini meliputi hal-hal sebagai berikut.", indent=False)
    add_numbered_item("1.", "Mengidentifikasi, menguji, dan menganalisis signifikansi kontribusi fitur meliputi feature importance dan local attribution yang membedakan transaksi promo pengguna baru sah dari akun tiruan menggunakan analisis interpretabilitas model berbasis TreeSHAP.")
    add_numbered_item("2.", "Mengembangkan, mengonfigurasi, dan mengevaluasi kinerja prediktif model XGBoost terhadap model pembanding menggunakan metrik evaluasi yang sensitif terhadap kelas minoritas meliputi precision-recall AUC, recall, precision, dan F1-score di bawah protokol penanganan ketidakseimbangan kelas.")
    add_numbered_item("3.", "Merancang formulasi kalibrasi probabilitas posterior dan mengonversinya menjadi indeks skor risiko kontinu berskala 0 hingga 100 dengan pembagian zona ambang batas mitigasi triase operasional meliputi auto-approve, step-up verification, dan voucher ineligible sebagai artefak pendukung keputusan.")

    add_subheading("1.5 Manfaat Penelitian")
    add_body_p("Secara teoretis, penelitian ini memberikan kontribusi ilmiah dalam pengembangan literatur Sistem Informasi, khususnya pada ranah Business Intelligence and Predictive Analytics. Penelitian ini memperkaya bukti empiris mengenai penerapan model gradient tree boosting pada domain pencegahan kecurangan insentif digital, sekaligus menjembatani kesenjangan teoretis antara pemodelan probabilitas komputasional dengan teori pengambilan keputusan sosioteknis dalam memitigasi risiko operasional tanpa menciptakan friksi bisnis yang destruktif.")
    
    add_body_p("Secara praktis, hasil penelitian ini menyediakan rancangan artefak dasbor pemantauan risiko bagi tim manajemen risiko dan operasional platform food delivery. Rancangan ini memberikan panduan terukur bagi para pengambil keputusan operasional untuk memutus motif ekonomi pelaku eksploitasi multi-akun, meminimalkan kebocoran anggaran pemasaran, dan menjaga akurasi metrik pertumbuhan pelanggan, sembari memastikan perjalanan transaksi bagi pelanggan baru yang sah tetap berlangsung lancar dan memuaskan.")

    add_subheading("1.6 Kebaruan Penelitian dan Celah Riset")
    add_body_p("Penelusuran sistematis terhadap literatur primer menunjukkan bahwa mayoritas riset terdahulu dalam deteksi penyalahgunaan promosi digital memperlakukan luaran model sebatas klasifikasi biner mutlak antara transaksi normal dan anomali. Pendekatan biner ini mengabaikan konsekuensi ekonomi operasional, sebab keputusan pemblokiran sepihak berisiko tinggi mengorbankan pelanggan baru sah pada program akuisisi komersial. Di samping itu, riset mutakhir skala besar cenderung mengandalkan arsitektur jaringan saraf graf GNN yang berfokus pada pemetaan sindikat terorganisir. Meskipun GNN unggul dalam memodelkan topologi jaringan akun, arsitektur tersebut menuntut konsumsi memori graf yang masif dan menghasilkan latensi inferensi mencapai beberapa detik hingga menit. Karakteristik latensi tersebut tidak memenuhi syarat toleransi waktu respons gerbang pembayaran checkout aplikasi pemesanan makanan yang menuntut eksekusi di bawah satu detik. Terdapat kekosongan literatur mengenai model berbasis data tabular ringan yang mengintegrasikan kalibrasi probabilitas posterior ke dalam indeks skor risiko bertingkat non-biner untuk mendukung tata kelola mitigasi yang proporsional pada akun baru tanpa riwayat historis cold-start.")

    add_body_p("Guna menegaskan diferensiasi metodologis dan lingkup variabel yang digunakan, pemetaan komparatif terhadap delapan penelitian primer terdahulu dilakukan dengan menyoroti domain transaksi, algoritma, serta keterbatasan dalam menangani transaksi perdana pada Tabel 1.1. Matriks ini memperlihatkan bahwa mayoritas rujukan mengasumsikan keberadaan profil historis pengguna yang telah mapan, sehingga menyisakan celah riset yang nyata pada deteksi cold-start akun baru platform pesan-antar makanan.")

    # Tabel 1.1 Matriks Literatur
    p_tbl1_cap = doc.add_paragraph()
    p_tbl1_cap.paragraph_format.space_before = Pt(8)
    p_tbl1_cap.paragraph_format.space_after = Pt(4)
    r_cap1 = p_tbl1_cap.add_run("Tabel 1.1 Matriks Perbandingan Penelitian Terdahulu yang Mendasari")
    r_cap1.bold = False
    r_cap1.font.size = Pt(11)

    lit_data = [
        ("No.", "Penulis & Tahun", "Judul & Publikasi", "Metode", "Hasil Utama", "Keterbatasan & Gap"),
        ("1", "Wen et al. (2023)", "Voucher Abuse Detection with Prompt-based Fine-tuning on GNN (ACM CIKM '23, DOI: 10.1145/3583780.3615505)", "VPGNN (Prompt-based GNN)", "Mengungguli model GNN konvensional dalam skenario label terbatas (few-shot anomaly detection).", "Kompleksitas graf bipartit tinggi; latensi inferensi lambat (kurang cocok untuk real-time checkout); black-box."),
        ("2", "Tian et al. (2024)", "CATeye: Coupled Attribute-Topology Invariance Learning (arXiv:2409.07062, diuji pada Lazada)", "CATeye (Graph Invariance Learning)", "Peningkatan rata-rata F1-score 8.61% menghadapi pergeseran distribusi lintas wilayah.", "Membutuhkan penyimpanan graf terdistribusi masif; fokus pada sindikat masif, kurang sensitif pada individual cold-start."),
        ("3", "Kumar et al. (2024)", "An intelligent approach to detect online fraud transaction using XGBoost (IJEECS, DOI: 10.11591/ijeecs.v35.i3.pp1491-1498)", "XGBoost Classifier", "Akurasi tinggi dan F1-Score stabil dalam deteksi transaksi keuangan digital.", "Keputusan biner kaku (fraud vs non-fraud); belum mengkaji kalibrasi skor risiko bertingkat dan belum diterapkan pada food delivery."),
        ("4", "Gupta et al. (2024)", "Enhancing Fraud Detection in Credit Card using XGBoost and SMOTE (IEEE ICSPCRE 2024, DOI: 10.1109/icspcre62303.2024.10675080)", "XGBoost + SMOTE", "Kombinasi XGBoost dan penanganan kelas tidak seimbang menekan False Negative secara signifikan.", "Fokus pada data kartu kredit sintetis Vesta; belum mengeksplorasi rekayasa fitur perilaku pesanan pertama (basket economics)."),
        ("5", "Chen & Guestrin (2016)", "XGBoost: A Scalable Tree Boosting System (ACM KDD '16, DOI: 10.1145/2939672.2939785)", "Gradient Tree Boosting", "Standar utama pemodelan data tabular terstruktur dengan komputasi paralel dan latensi minimal.", "Studi fondasi algoritma; tidak secara otomatis menyediakan model mitigasi bisnis tanpa desain pasca-pemrosesan."),
        ("6", "Lundberg & Lee (2017)", "A Unified Approach to Interpreting Model Predictions (NeurIPS 2017, Vol. 30)", "TreeSHAP (Explainable AI)", "Atribusi fitur aditif konsisten lokal dan global berbasis teori permainan kooperatif.", "Instrumen diagnostik murni; memerlukan integrasi ke alur pendukung keputusan operasional."),
        ("7", "Niculescu-Mizil & Caruana (2005)", "Predicting Good Probabilities With Supervised Learning (ACM ICML '05, DOI: 10.1145/1102351.1102430)", "Platt Scaling & Isotonic Regression", "Membuktikan raw margin boosting terdistorsi dan kalibrasi pasca-latih meningkatkan keandalan probabilitas.", "Tidak merancang skenario ambang batas operasional multi-level untuk tata kelola pencegahan kecurangan promosi."),
        ("8", "Fiarni et al. (2022)", "Detection System of Promotion Abuse Using Similarity and Risk Scoring (JNTETI Sinta 2, DOI: 10.22146/jnteti.v11i3.3743)", "Similarity Matching & Heuristic Risk Scoring", "Precision dan recall tinggi dalam mendeteksi keterkaitan multi-akun promosi pada transaksi lokal.", "Bergantung pada aturan pembobotan manual dan jarak teks statis yang rapuh terhadap variasi ejaan; belum menggunakan machine learning adaptif non-linear."),
        ("9", "Penelitian Diusulkan (2026)", "Pengembangan Model Risk Scoring Berbasis XGBoost untuk Mendukung Mitigasi Promo Abuse Food Delivery", "XGBoost + Kalibrasi + Risk Scoring Bertingkat (Low/Med/High)", "Skor risiko terkalibrasi (0-100), penjelasan fitur TreeSHAP, dan skenario mitigasi proporsional.", "Mengisi gap efisiensi komputasi checkout instan, mitigasi adaptif non-biner, dan penanganan cold-start akun perdana.")
    ]

    tbl_lit = doc.add_table(rows=len(lit_data), cols=6)
    tbl_lit.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_lit.autofit = False
    col_w_lit = [Cm(0.8), Cm(2.5), Cm(3.5), Cm(2.4), Cm(3.2), Cm(3.6)]
    set_table_borders(tbl_lit)

    for r_idx, row_vals in enumerate(lit_data):
        row = tbl_lit.rows[r_idx]
        is_header = (r_idx == 0)
        is_proposed = (r_idx == len(lit_data) - 1)
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_w_lit[c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if (c_idx == 0 or is_header) else WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_runs(p, val, base_size=Pt(9.5) if not is_header else Pt(10), default_bold=is_header or is_proposed)
            if is_header:
                set_cell_background(cell, "E0E0E0")
            elif is_proposed:
                set_cell_background(cell, "F2F2F2")
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

    p_after_tbl = doc.add_paragraph()
    p_after_tbl.paragraph_format.space_before = Pt(8)
    add_body_p("Kebaruan penelitian ini terletak pada integrasi arsitektural antara algoritma pembelajaran mesin XGBoost yang dioptimasi untuk kecepatan inferensi tabular sub-second, teknik kalibrasi probabilitas posterior, dan formulasi indeks skor risiko bertingkat. Berbeda dari pendekatan biner terdahulu, kerangka kerja ini secara eksplisit mengaitkan estimasi risiko numerik dengan kebijakan intervensi operasional yang proporsional, serta melengkapinya dengan interpretabilitas fitur TreeSHAP guna memberikan transparansi alasan penilaian bagi analis risiko platform.")

    # ==================== BAB 2 KAJIAN PUSTAKA ====================
    doc.add_page_break()
    add_chapter_title("BAB 2", "KAJIAN PUSTAKA")

    add_subheading("2.1 Tinjauan Pustaka")
    add_body_p("Evolusi metode pendeteksian anomali dan kecurangan transaksi digital dalam literatur mutakhir terpolarisasi ke dalam dua pendekatan metodologis utama, yaitu pendekatan berbasis pemodelan graf dan pendekatan berbasis pohon keputusan bergradien pada data tabular.")
    
    add_body_p("Pendekatan berbasis graf, seperti yang dikembangkan oleh Wen et al. (2023) melalui VPGNN dan Tian et al. (2024) melalui kerangka CATeye pada ekosistem belanja daring, memodelkan entitas pengguna, perangkat keras, alamat IP, dan voucher sebagai simpul dalam graf heterogen. Keunggulan utama dari pendekatan ini adalah kemampuannya membongkar sindikat kecurangan terorganisir berskala besar melalui perambatan relasi struktural. Kendati demikian, pemrosesan graf skala industri menuntut sumber daya memori graf terdistribusi yang sangat besar dan menghasilkan latensi penelusuran relasi yang mencapai hitungan detik hingga puluhan detik. Dalam operasional aplikasi pesan-antar makanan, transaksi pembelian berlangsung secara seketika, sehingga proses validasi kelayakan promo pada gerbang pembayaran checkout menuntut batas toleransi waktu eksekusi ketat di bawah satu detik. Kendala latensi ini menjadikan model graf sulit diimplementasikan secara langsung pada titik intervensi transaksi individual.")

    add_body_p("Di samping pendekatan graf dan pohon keputusan, literatur pencegahan kecurangan promosi di Indonesia juga mencatat pendekatan berbasis pencocokan kemiripan dan sistem penilaian risiko heuristik. Fiarni et al. (2022) mengidentifikasi tujuh atribut transaksi penting pada e-commerce Indonesia, meliputi informasi jaringan, kontak, alamat, dan instrumen pembayaran, serta merancang sistem penilaian risiko berbasis jarak kemiripan teks Levenshtein. Meskipun efektif mendeteksi duplikasi identitas sederhana, sistem berbasis aturan statis dan kemiripan teks tersebut rentan mengalami penurunan akurasi ketika menghadapi manipulasi penulisan alamat atau pergantian instrumen digital. Temuan Fiarni et al. (2022) menegaskan pentingnya seleksi atribut transaksi lokal, yang dalam penelitian ini ditingkatkan kapabilitasnya menggunakan algoritma pembelajaran mesin adaptif XGBoost agar mampu menangkap pola kecurangan non-linear secara probabilistik.")

    add_body_p("Sebaliknya, pendekatan berbasis pohon keputusan bergradien pada data terstruktur, yang dipelopori oleh Chen & Guestrin (2016) serta diuji dalam ranah transaksi keuangan oleh Kumar et al. (2024) dan Gupta et al. (2024), menunjukkan superioritas performa pada data tabular. Algoritma XGBoost secara konsisten mampu memproses pola interaksi non-linear antarfitur dengan kecepatan komputasi tinggi, konsumsi memori rendah, serta ketahanan alami terhadap nilai data yang hilang. Walaupun demikian, kelemahan mendasar dari sebagian besar implementasi XGBoost terdahulu adalah orientasi keluarannya yang diperlakukan sebatas klasifikasi biner kaku. Pada transaksi promosi komersial, vonis pemblokiran mutlak terbukti kontraproduktif karena meningkatkan risiko penolakan pelanggan sah false positive. Oleh karena itu, penggabungan efisiensi tabular XGBoost dengan kalibrasi skor risiko bertingkat menjadi jembatan metodologis yang esensial untuk menjawab kebutuhan tata kelola promosi modern.")

    add_subheading("2.2 Landasan Teoretik")

    add_subsubheading("2.2.1 Promotional Abuse dalam Ekosistem Layanan Pesan-Antar Makanan")
    add_body_p("Promotional abuse merupakan bentuk pelanggaran ketentuan operasional ketika pengguna mengeksploitasi mekanisme insentif platform digital untuk memperoleh keuntungan finansial di luar batasan peruntukan yang sah. Dalam ekosistem layanan pesan-antar makanan di Indonesia seperti GoFood, program akuisisi konsumen baru umumnya memberikan subsidi voucher diskon transaksi perdana dengan nilai pemotongan yang besar dan syarat pembelanjaan minimum. Modus operandi yang paling kerap ditemukan pada program ini adalah pembuatan pembuatan akun tiruan massal. Pelaku memanfaatkan layanan penyedia nomor ponsel virtual instan guna mendaftarkan akun baru secara massal, kemudian memanfaatkan kode promosi diskon perdana untuk melakukan pemesanan makanan berulang kali. Berbeda dari penipuan transaksi keuangan konvensional yang melibatkan pencurian kartu kredit atau pengambilalihan akun secara ilegal, transaksi penyalahgunaan promosi umumnya menggunakan dana pembayaran yang sah, seperti saldo GoPay, transfer bank, atau tunai,, tetapi melanggar batasan eligibilitas promosi yang telah ditetapkan perusahaan.")

    add_subsubheading("2.2.2 Perspektif Sistem Informasi dalam Tata Kelola Risiko Promosi")
    add_body_p("Dalam disiplin ilmu Sistem Informasi, penanganan kecurangan promosi tidak dapat diselesaikan semata-mata melalui optimasi algoritma komputasi di laboratorium, melainkan harus dipandang melalui lensa Teori Sosioteknis yang dirumuskan oleh Bostrom & Heinen (1977) dan Leavitt (1965). Teori ini menegaskan bahwa keberhasilan sistem organisasi bergantung pada keselarasan timbal balik antara subsistem teknis dan subsistem sosial.")
    
    add_body_p("Dalam konteks mitigasi promotional abuse pada platform food delivery seperti GoFood, pilar Technology menyediakan infrastruktur pemrosesan data tabular dan model pembelajaran mesin XGBoost yang mengevaluasi risiko transaksi secara objektif di gerbang pre-checkout. Pilar People mencakup dinamika perilaku multi-aktor: konsumen pemesan makanan, baik pelanggan sah organik maupun pelaku eksploitasi multi-akun,, mitra merchant resto yang mengandalkan keadilan perputaran pesanan, mitra pengemudi yang mengantar makanan, serta analis risiko yang membutuhkan transparansi alasan inferensi sebelum menetapkan kebijakan operasional. Pilar Process merepresentasikan rangkaian alur bisnis pemesanan makanan, mulai dari pemilihan menu resto, penambahan item ke keranjang belanja, peninjauan dan penerapan voucher diskon saat pre-checkout, hingga eksekusi verifikasi bertahap. Terakhir, pilar Organization mengendalikan tata kelola alokasi subsidi promosi divisi pemasaran dan memastikan bahwa perlindungan anggaran pemasaran tidak mengganggu pencapaian target akuisisi pelanggan baru maupun citra kepuasan pengguna. Integrasi keempat pilar ini menjamin bahwa model yang dikembangkan selaras dengan kebutuhan strategis bisnis platform, melalui interaksi timbal-balik antara teknologi prediktif, proses bisnis, pengguna, dan tata kelola organisasi yang membentuk satu kesatuan ekosistem pengendalian risiko, seperti ditunjukkan pada Gambar 2.1.")

    # GAMBAR 2.1
    add_figure("gambar_2_1_kerangka_sosioteknis.png", "Gambar 2.1  Kerangka Sosioteknis Sistem Informasi dalam Tata Kelola Risiko Promosi", width_cm=13.5)

    add_subsubheading("2.2.3 Algoritma Extreme Gradient Boosting XGBoost")
    add_body_p("XGBoost merupakan algoritma pembelajaran mesin terawasi berbasis ensemble tree yang bekerja secara aditif dengan meminimalkan fungsi objektif teratur. Pada iterasi ke-t, fungsi objektif yang diminimalkan dinyatakan sebagai:")
    
    add_equation_box("L^(t) = Σ l(y_i, y_hat_i^(t-1) + f_t(x_i)) + Ω(f_t)")
    
    add_body_p("Pada persamaan ini, l melambangkan fungsi kerugian terbedakan konveks yang mengukur deviasi antara label aktual y_i dan nilai prediksi y_hat_i, sedangkan f_t(x_i) melambangkan struktur pohon keputusan baru yang ditambahkan pada iterasi tersebut. Suku penalti regularisasi Ω(f_t) berfungsi membatasi kompleksitas struktur pohon guna mencegah fenomena overfitting, yang didefinisikan sebagai:")
    
    add_equation_box("Ω(f_t) = γ T + 0.5 λ Σ w_j^2")
    
    add_body_p("Dengan T melambangkan jumlah daun, w_j merepresentasikan bobot skor pada daun ke-j, serta γ dan λ bertindak sebagai konstanta penalti kompleksitas dan bobot regularisasi L2.")
    
    add_body_p("Untuk menangani ketidakseimbangan kelas ekstrem yang umum terjadi pada data transaksi kecurangan, XGBoost memodifikasi perhitungan turunan gradien fungsi kerugian logistik melalui penyertaan parameter penyeimbang bobot kelas positif w atau scale_pos_weight. Modifikasi fungsi kerugian berbobot dinyatakan sebagai:")
    
    add_equation_box("L_cost(y_i, p_hat_i) = - [ w * y_i * log(p_hat_i) + (1 - y_i) * log(1 - p_hat_i) ]")
    
    add_body_p("Nilai bobot w dikonfigurasi berdasarkan rasio jumlah sampel negatif terhadap sampel positif (w = N_neg / N_pos), sehingga penalti atas kesalahan prediksi pada kelas minoritas kecurangan ditingkatkan secara proporsional.")

    add_subsubheading("2.2.4 Teori Kalibrasi Probabilitas")
    add_body_p("Meskipun algoritma boosted trees memiliki kapabilitas pemisahan kelas yang sangat baik, nilai margin keluaran mentah yang ditransformasikan oleh fungsi sigmoid sering kali terdistorsi dan tidak mencerminkan probabilitas posterior yang sesungguhnya (Niculescu-Mizil & Caruana, 2005). Nilai probabilitas mentah cenderung terkonsentrasi menjauhi nilai ekstrem atau mengalami deviasi sistemik akibat penalti regularisasi dan pembobotan kelas.")
    
    add_body_p("Untuk memulihkan validitas empiris dari estimasi risiko, probabilitas keluaran dikalibrasi pasca-pelatihan menggunakan metode Platt Scaling atau Isotonic Regression. Platt Scaling menerapkan transformasi parametrik regresi logistik univariat terhadap margin keluaran model f(x):")
    
    add_equation_box("P(y_i = 1 | f_i) = 1 / (1 + exp(A * f_i + B))")
    
    add_body_p("Parameter skalar A dan B diestimasi melalui optimasi maximum likelihood pada data validasi terpisah. Sementara itu, Isotonic Regression mengadopsi pendekatan non-parametrik menggunakan algoritma Pool Adjacent Violators untuk memetakan margin ke fungsi monoton naik bertahap. Keandalan kalibrasi probabilitas diuji secara kuantitatif menggunakan metrik Brier Score:")
    
    add_equation_box("BS = (1 / N) * Σ (p_hat_i - y_i)^2")
    
    add_body_p("Semakin kecil nilai Brier Score, semakin akurat probabilitas model dalam merefleksikan frekuensi kejadian kecurangan yang sebenarnya di dunia nyata.")

    add_subsubheading("2.2.5 Interpretabilitas Model Menggunakan TreeSHAP")
    add_body_p("Penerapan sistem pendukung keputusan di industri menuntut adanya akuntabilitas dan transparansi penalaran model. Dalam penelitian ini, interpretabilitas model diwujudkan melalui algoritma TreeSHAP (Lundberg & Lee, 2017) yang menurunkan atribusi fitur aditif berdasarkan nilai Shapley dari teori permainan kooperatif:")
    
    add_equation_box("φ_i(x) = Σ [ (|S|! * (|F| - |S| - 1)!) / |F|! ] * [ f_x(S ∪ {i}) - f_x(S) ]")
    
    add_body_p("Notasi φ_i(x) mengukur kontribusi marjinal fitur ke-i terhadap selisih antara prediksi model f_x untuk instans transaksi tertentu dengan nilai rata-rata dasar prediksi pada seluruh dataset. TreeSHAP memberikan dua tingkatan penjelasan: penjelasan global untuk mengidentifikasi fitur yang mendominasi risiko secara sistemik, dan penjelasan lokal melalui waterfall plot untuk menguraikan alasan spesifik kenaikan skor risiko pada transaksi individual yang sedang ditinjau oleh analis.")

    add_subsubheading("2.2.6 Analisis Kritis Keterbatasan Algoritma XGBoost pada Domain Fraud")
    add_body_p("Meskipun algoritma XGBoost dipilih sebagai mesin inferensi utama, evaluasi akademik yang objektif menuntut pengakuan terhadap limitasi inheren metode ini. XGBoost bekerja pada representasi data tabular baris-per-baris, sehingga secara alamiah tidak memiliki kapabilitas bawaan untuk menangkap relasi struktural graf multi-langkah. Pola kecurangan canggih yang melibatkan perputaran identitas dalam sindikat cincin perangkat yang terdistribusi lintas waktu sulit dimodelkan secara langsung tanpa rekayasa fitur manual yang rumit. Selain itu, fitur akselerasi transaksi berbasis waktu seperti frekuensi pesanan per subnet IP dalam 24 jam bergantung pada batas jendela waktu yang kaku yang dapat dimanipulasi oleh pelaku yang sengaja memperlambat laju serangannya. Kendati demikian, trade-off ini diterima secara rasional karena efisiensi komputasi data tabular XGBoost menjamin latensi inferensi sub-second saat transaksi berlangsung di gerbang pembayaran, suatu keunggulan operasional yang tidak dapat dipenuhi oleh arsitektur graf yang lambat.")

    add_subheading("2.3 Kerangka Berpikir")
    add_body_p("Penelitian ini dibangun di atas kerangka penalaran logis yang menjembatani fenomena empiris industri dengan perancangan artefak teknologi informasi. Alur kerangka berpikir berawal dari identifikasi masalah kebocoran anggaran pemasaran akibat eksploitasi multi-akun pada program promosi pengguna baru layanan food delivery. Kelemahan mekanisme aturan statis yang kaku dan memicu tingginya angka salah blokir menjadi landasan urgensi bagi perancangan model penilaian risiko probabilistik.")
    
    add_body_p("Data transaksi perdana akun baru diekstraksi ke dalam dimensi temporal, ekonomi keranjang belanja, akselerasi jaringan, dan kemiripan spasial. Data tersebut diproses oleh algoritma XGBoost dengan penanganan ketidakseimbangan kelas untuk menghasilkan probabilitas risiko. Keluaran probabilitas kemudian dikalibrasi guna menjamin keandalan estimasi, sebelum ditransformasikan menjadi indeks skor risiko kontinu berskala 0 hingga 100. Skor risiko ini dipetakan ke dalam zona intervensi triase operasional yang didukung oleh transparansi fitur TreeSHAP, sehingga menghasilkan sistem pendukung keputusan yang mampu melindungi efisiensi subsidi pemasaran sekaligus menjaga kelancaran transaksi bagi konsumen baru organik. Alur penalaran logis dari identifikasi masalah sosioteknis hingga perancangan artefak pendukung keputusan ini dirangkum secara utuh, seperti disajikan pada Gambar 2.2.")

    # GAMBAR 2.2
    add_figure("gambar_2_2_kerangka_berpikir.png", "Gambar 2.2  Diagram Alur Kerangka Berpikir Penelitian", width_cm=14.5)

    # ==================== BAB 3 METODE PENELITIAN ====================
    doc.add_page_break()
    add_chapter_title("BAB 3", "METODE PENELITIAN")

    add_subheading("3.1 Pendekatan, Jenis, dan Prosedur Penelitian")
    add_body_p("Penelitian ini menggunakan pendekatan kuantitatif eksperimental berbasis metodologi ilmu desain Design Science Research yang merujuk pada kerangka kerja pengembangan artefak sistem informasi (Hevner et al., 2004). Jenis penelitian adalah penelitian terapan komparatif yang menguji performa prediktif dan efisiensi algoritma XGBoost secara empiris terhadap model baseline linier logistic regression dan pohon keputusan decision tree. Prosedur penelitian mengadaptasi kerangka kerja standar industri CRISP-DM (Chapman et al., 2000) yang dioperasionalkan ke dalam enam tahapan akademik yang saling berkesinambungan.")
    
    add_body_p("Tahapan kerja diawali dengan pemahaman konteks bisnis guna memetakan alur klaim voucher promosi pengguna baru serta merumuskan parameter keberhasilan mitigasi risiko. Tahap kedua mencakup penelaahan dan penelaahan data untuk mengaudit kelayakan data log transaksi, menganalisis rasio ketidakseimbangan kelas, serta memvalidasi integritas label kecurangan. Tahap ketiga berfokus pada persiapan data, meliputi penanganan nilai kosong berbasis sifat bawaan algoritma, penyelarasan format data tabular, dan ekstraksi fitur perilaku transaksi perdana.")
    
    add_body_p("Tahap keempat merupakan pemodelan komparatif, yang mencakup pembagian data berbasis kronologis waktu, optimasi hiperparameter melalui validasi silang berstrata 5-fold, serta pelatihan model XGBoost bersama model pembanding. Tahap kelima adalah evaluasi dan kalibrasi untuk menilai kinerja model menggunakan metrik kelas tidak seimbang, mengalibrasi probabilitas mentah pasca-latih, dan mengurai nilai atribusi fitur menggunakan TreeSHAP. Tahap keenam adalah perancangan artefak pendukung keputusan, yang diwujudkan melalui prototipe antarmuka dasbor pemantauan risiko simulatif berbasis Streamlit untuk memandu eksekusi mitigasi operasional yang proporsional. Keseluruhan tahapan iteratif dari pemahaman bisnis hingga penyusunan artefak prototipe ini terstruktur dalam adaptasi alur kerja CRISP-DM, seperti disajikan pada Gambar 3.1.")

    # GAMBAR 3.1
    add_figure("gambar_3_1_prosedur_crisp_dm.png", "Gambar 3.1  Prosedur Penelitian Pengembangan Model Berbasis Adaptasi CRISP-DM", width_cm=14.5)

    add_subheading("3.2 Objek dan Sumber Data")
    add_body_p("Objek penelitian ini adalah rekaman data transaksi dan aktivitas klaim voucher promosi pengguna baru pada platform layanan pesan-antar makanan digital, dengan acuan alur operasional dan karakteristik fitur mengacu secara empiris pada ekosistem GoFood di Indonesia. Unit analisis ditetapkan secara spesifik pada transaksi pesanan perdana per akun pada titik evaluasi sebelum pesanan dikonfirmasi pada tahap pre-checkout. Pemilihan unit analisis ini didasarkan pada kebutuhan riil industri untuk mencegah kebocoran subsidi promosi secara seketika sebelum transaksi dialihkan ke gerbang pembayaran bank atau mitra pengemudi.")
    
    add_body_p("Guna menjamin validitas empiris sekaligus memastikan kepatuhan hukum terhadap privasi data, proses seleksi dilakukan melalui audit komparatif terhadap empat kandidat sumber data, sebagaimana dirangkum pada Tabel 3.1. Penilaian ini menimbang relevansi fitur terhadap perilaku promosi, keterbukaan akses publik, serta ketiadaan informasi identitas pribadi Zero PII sebelum menetapkan basis data sekunder yang digunakan.")

    # Tabel 3.1 Kandidat Dataset
    p_tbl2_cap = doc.add_paragraph()
    p_tbl2_cap.paragraph_format.space_before = Pt(8)
    p_tbl2_cap.paragraph_format.space_after = Pt(4)
    r_cap2 = p_tbl2_cap.add_run("Tabel 3.1 Matriks Evaluasi Kelayakan Kandidat Dataset")
    r_cap2.bold = False
    r_cap2.font.size = Pt(11)

    ds_eval_data = [
        ("Parameter Evaluasi", "DS-CAND-01: IEEE-CIS", "DS-CAND-02: Alibaba O2O", "DS-CAND-03: Mitra Food Delivery", "DS-CAND-04: Data Sintetis"),
        ("Sumber & Publikasi", "Vesta Corp / Kaggle (2019)", "Alibaba Tianchi Platform (2016)", "Mitra Industri / Merchant Food Delivery", "Generator CTGAN / Aturan Buatan"),
        ("Kesesuaian Domain", "Transaksi kartu kredit e-commerce", "Pola kupon ritel fisik", "Klaim promo perdana food delivery", "Simulasi numerik buatan"),
        ("Unit Analisis", "Transaksi pembayaran", "Interaksi User-Coupon", "Pesanan perdana akun baru (cold-start)", "Baris transaksi sintetis artifisial"),
        ("Target Label", "isFraud (fraud kartu kredit)", "Date terisi (kupon dipakai)", "is_promo_abuse (multi-akun terkonfirmasi)", "Label acak aturan generator"),
        ("Validitas Ground-Truth", "Tervalidasi (Audit Vesta)", "Tidak Valid (Konversi != Fraud)", "Menunggu audit tim fraud mitra", "Tidak Valid (Bukan fenomena riil)"),
        ("Kepatuhan Privasi", "Terbuka untuk umum (Lisensi Kaggle)", "Terbuka riset akademik", "Perlu NDA & PKS (Zero PII)", "Terbuka penuh"),
        ("Keputusan Audit Desain", "Ditolak (Domain kartu kredit)", "Ditolak (Konversi bukan fraud)", "Kandidat Utama (Audit di M6)", "Ditolak (Bukan data uji utama)")
    ]

    tbl_ds = doc.add_table(rows=len(ds_eval_data), cols=5)
    tbl_ds.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ds.autofit = False
    col_w_ds = [Cm(2.6), Cm(3.5), Cm(3.5), Cm(4.0), Cm(3.4)]
    set_table_borders(tbl_ds)

    for r_idx, row_vals in enumerate(ds_eval_data):
        row = tbl_ds.rows[r_idx]
        is_header = (r_idx == 0)
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_w_ds[c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx == 0) else WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_runs(p, val, base_size=Pt(9.5) if not is_header else Pt(10), default_bold=is_header or ("Ditolak" in val) or ("Kandidat Utama" in val))
            if is_header:
                set_cell_background(cell, "E0E0E0")
            elif "Kandidat Utama" in val:
                set_cell_background(cell, "FFF2CC")
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

    p_after_ds = doc.add_paragraph()
    p_after_ds.paragraph_format.space_before = Pt(8)
    add_body_p("Penelitian ini menetapkan aturan perubahan desain riset sebagai mekanisme kontingensi legal. Apabila akses fisik terhadap data sekunder industri DS-CAND-03 terkendala oleh proses perizinan formal korporasi pasca-seminar proposal, peneliti mematuhi kebijakan integritas data mutlak tanpa melakukan pemalsuan dataset. Peneliti wajib mengaktifkan salah satu opsi kontingensi resmi atas persetujuan Dosen Pembimbing: Opsi Kontingensi A, yaitu mengalihkan objek empiris ke dataset patokan transaksi digital terbuka bereputasi, seperti IEEE-CIS Fraud Benchmark atau Alibaba User Behavior Dataset, yang memiliki label anomali terverifikasi publik melalui skema pemetaan fitur temporal, nilai pesanan, dan frekuensi jaringan; atau Opsi Kontingensi B, yaitu mengajukan permohonan data sekunder teranomalisasi ke penyedia layanan dompet digital atau agregator pembayaran alternatif yang memiliki skema riset akademik resmi.")
    add_body_p("Guna menjamin keandalan data sekunder sebelum diproses dalam pipeline pemodelan, penelitian ini menerapkan prosedur pemeriksaan mutu dan kewajaran label sanity check. Pemeriksaan ini dilakukan melalui analisis integritas data untuk mengidentifikasi keberadaan label kontradiktif, yakni transaksi dengan pola fitur yang serupa namun memiliki label kelas yang berbeda, serta menyaring data anomali yang tidak logis. Baris data yang terindikasi memiliki ambiguitas label dieksklusikan dari himpunan data latih guna mencegah distorsi inferensi pada model XGBoost.")

    add_subheading("3.3 Variabel dan Definisi Operasional")
    add_body_p("Operasionalisasi variabel dalam penelitian ini mencakup satu target klasifikasi biner dan 14 fitur prediktor yang dikelompokkan ke dalam empat dimensi perilaku transaksi pre-checkout, sebagaimana tercantum pada Tabel 3.2. Setiap fitur dirancang secara spesifik untuk menangkap indikasi ketidakwajaran akun baru tanpa bergantung pada data riwayat masa lalu.")

    # Tabel 3.2 Variabel & Fitur
    p_tbl3_cap = doc.add_paragraph()
    p_tbl3_cap.paragraph_format.space_before = Pt(8)
    p_tbl3_cap.paragraph_format.space_after = Pt(4)
    r_cap3 = p_tbl3_cap.add_run("Tabel 3.2 Definisi Operasional Variabel Penelitian dan Kelompok Fitur")
    r_cap3.bold = False
    r_cap3.font.size = Pt(11)

    var_data = [
        ("Kategori Variabel", "Nama Variabel / Fitur", "Tipe Data & Skala", "Definisi Operasional", "Rasionalitas Hubungan terhadap Risiko"),
        ("Target Label (Y)", "is_promo_abuse", "Biner (y ∈ {0, 1})", "Bernilai 1 jika pesanan terbukti klaim tidak sah akun duplikasi; 0 jika organik sah.", "Label ground-truth hasil verifikasi tim manajemen risiko platform."),
        ("Fitur Temporal", "account_age_seconds", "Numerik Kontinu (Detik)", "Selisih waktu (detik) sejak akun terdaftar hingga penekanan checkout promo perdana.", "Mendeteksi pola klaim instan skrip otomatis. Kendati sindikat mengendapkan akun baru (sleeper accounts), model tetap mampu mengenali risiko lewat interaksi non-linear dengan fitur pembayaran berulang dan klaster alamat."),
        ("Fitur Temporal", "time_since_install", "Numerik Kontinu (Menit)", "Rentang waktu (menit) dari instalasi aplikasi hingga transaksi pertama dilakukan.", "Mendeteksi akun instan pada lingkungan emulator atau perangkat baru reset."),
        ("Ekonomi Keranjang", "order_total_amount", "Numerik Kontinu (Rupiah)", "Akumulasi nilai belanja kotor pesanan sebelum pemotongan diskon promo.", "Mengukur skala ekonomi pesanan dan proporsi subsidi yang diklaim."),
        ("Ekonomi Keranjang", "discount_amount", "Numerik Kontinu (Rupiah)", "Besaran nominal subsidi potongan harga yang diklaim melalui voucher promo.", "Mengukur besaran nilai subsidi finansial yang berisiko bocor."),
        ("Ekonomi Keranjang", "discount_ratio", "Numerik Rasio ([0.0, 1.0])", "Rasio antara nominal diskon promosi dibagi total nilai belanja kotor.", "Rasio diskon ekstrem mendekati batas maksimal mengindikasikan eksploitasi agresif."),
        ("Ekonomi Keranjang", "is_min_spend_exact", "Biner (x ∈ {0, 1})", "Bernilai 1 jika belanja dalam toleransi 5% dari ambang minimum promo; 0 lainnya.", "Pola tipikal akun sybil yang memesan sehemat mungkin demi diskon maksimal."),
        ("Akselerasi Jaringan", "orders_per_subnet_24h", "Numerik Diskrit (Frekuensi)", "Akumulasi pesanan promo akun baru dari blok subnet IP /24 yang sama dalam 24 jam.", "Mendeteksi klaster pendaftaran massal dari jaringan WiFi bersama atau proxy."),
        ("Akselerasi Jaringan", "orders_per_device_group_24h", "Numerik Diskrit (Frekuensi)", "Frekuensi transaksi klaim promo dari fingerprint perangkat identik dalam 24 jam.", "Sinyal kuat satu perangkat fisik menjalankan banyak akun secara bergantian."),
        ("Kemiripan Spasial", "address_cluster_frequency", "Numerik Diskrit (Frekuensi)", "Akumulasi pesanan promo akun baru pada radius spasial identik via pembulatan koordinat GPS (toleransi 50 meter) guna mengatasi variasi teks alamat.", "Mengungkap anomali puluhan akun baru memesan ke titik fisik yang identik, terlepas dari manipulasi singkatan nama jalan oleh pelaku."),
        ("Integrasi Pembayaran", "payment_instrument_reuse_count", "Numerik Diskrit (Frekuensi)", "Frekuensi penggunaan instrumen pembayaran digital (seperti ID sumber dana GoPay, kartu debit/kredit, atau akun bank) yang sebelumnya pernah terhubung ke akun lain.", "Sinyal kuat keterkaitan fisik antar-akun meskipun identitas pendaftaran nomor telepon tampak baru.")
    ]

    tbl_var = doc.add_table(rows=len(var_data), cols=5)
    tbl_var.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_var.autofit = False
    col_w_var = [Cm(2.6), Cm(3.6), Cm(2.0), Cm(4.4), Cm(4.4)]
    set_table_borders(tbl_var)

    for r_idx, row_vals in enumerate(var_data):
        row = tbl_var.rows[r_idx]
        is_header = (r_idx == 0)
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_w_var[c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx in [0, 2]) else WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_runs(p, val, base_size=Pt(9.5) if not is_header else Pt(10), default_bold=is_header or (c_idx == 0 and "Target" in val))
            if is_header:
                set_cell_background(cell, "E0E0E0")
            elif c_idx == 0 and "Target" in val:
                set_cell_background(cell, "FBE5D6")
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

    p_after_var = doc.add_paragraph()
    p_after_var.paragraph_format.space_before = Pt(8)

    add_subheading("3.4 Desain Eksperimen dan Pemodelan XGBoost")
    add_body_p("Prosedur eksperimen dirancang untuk menguji performa model secara objektif sekaligus merefleksikan kondisi operasional sistem di dunia nyata. Pemisahan data menerapkan protokol penahanan berbasis waktu holdout split, di mana seluruh catatan transaksi diurutkan secara kronologis dan dibagi menjadi 70% data latih awal, 15% data validasi tuning, dan 15% data uji holdout masa depan. Protokol ini mencegah terjadinya kebocoran informasi masa depan data leakage, suatu kesalahan fatal yang kerap terjadi jika data transaksi dipisahkan menggunakan pengacakan konvensional.")
    
    add_body_p("Pencegahan kebocoran data juga ditegakkan secara ketat pada penetapan titik prediksi pre-checkout. Model hanya diizinkan memproses atribut yang telah tersedia secara pasti pada saat pengguna menekan tombol peninjauan pesanan. Seluruh atribut yang baru terwujud setelah pesanan berhasil dibuat, meliputi waktu penugasan mitra pengemudi, durasi pengantaran pesanan, maupun penilaian ulasan makanan, dilarang keras digunakan dalam rekayasa fitur pemodelan. Alur pemrosesan data mulai dari penetapan batas pre-checkout hingga penyiapan data latih ini terangkum dalam arsitektur pipeline eksperimen, sebagaimana diilustrasikan pada Gambar 3.2.")

    # GAMBAR 3.2
    add_figure("gambar_3_2_pipeline_pemodelan.png", "Gambar 3.2  Arsitektur Pipeline Rekayasa Fitur dan Pemodelan XGBoost", width_cm=14.5)

    add_body_p("Penanganan ketidakseimbangan kelas dilakukan melalui evaluasi komparatif antara metode penyeimbangan biaya internal XGBoost dan metode penyeimbangan data. Pada metode internal, parameter scale_pos_weight dikonfigurasi berdasarkan rasio sampel negatif terhadap positif (N_neg / N_pos) untuk meningkatkan penalti kerugian kelas minoritas. Kinerja pendekatan ini dibandingkan terhadap teknik SMOTE dan Random Under-Sampling yang hanya diaplikasikan pada data latih.")

    add_body_p("Proses optimasi hiperparameter XGBoost dilakukan secara sistematis pada data latih menggunakan Stratified 5-Fold Cross-Validation. Ruang pencarian hiperparameter mencakup laju pembelajaran (learning_rate: 0.01 hingga 0.1), kedalaman maksimum pohon (max_depth: 3 hingga 6), jumlah pohon estimator (n_estimators: 100 hingga 500 dengan mekanisme early stopping 20 iterasi), serta fraksi pemilihan sampel dan fitur (subsample: 0.7 hingga 1.0; colsample_bytree: 0.7 hingga 1.0). Konfigurasi terbaik yang dihasilkan kemudian dilatih dan dievaluasi terhadap model pembanding Logistic Regression dan Decision Tree pada data uji independen.")

    add_subheading("3.5 Evaluasi dan Rancangan Decision Support")
    add_body_p("Mengingat distribusi data kecurangan yang sangat timpang, evaluasi performa prediktif tidak mengandalkan metrik akurasi, melainkan berpusat pada metrik evaluasi kurva presisi-recall. Metrik performa utama yang digunakan adalah Precision-Recall Area Under Curve PR-AUC atau Average Precision AP, yang didefinisikan secara matematis sebagai:")
    
    add_equation_box("AP = Σ (R_k - R_(k-1)) * P_k")
    
    add_body_p("Notasi P_k dan R_k melambangkan presisi dan daya tangkap recall pada ambang batas ke-k. Evaluasi dilengkapi dengan metrik Recall untuk mengukur proporsi akun kecurangan yang berhasil dijaring, Precision untuk mengukur kepastian bahwa akun yang dicurigai benar-benar merupakan akun abusif, nilai F1-Score, serta matriks kebingungan confusion matrix. Keandalan estimasi probabilitas diuji menggunakan Brier Score sebelum dan sesudah kalibrasi.")

    add_body_p("Probabilitas risiko terkalibrasi (P_calibrated ∈ [0.0, 1.0]) kemudian ditransformasikan secara linier ke dalam indeks skor risiko kontinu berskala 0 hingga 100:")
    
    add_equation_box("Risk Score = P_calibrated * 100")
    
    add_body_p("Berdasarkan distribusi probabilitas terkalibrasi, sistem menetapkan dua nilai ambang batas dinamis yang membagi keputusan mitigasi ke dalam tiga zona triase operasional, sebagaimana dirangkum pada Tabel 3.3. Pembagian zona ini memastikan bahwa tindakan penolakan promo hanya dikenakan pada pesanan dengan bukti anomali ekstrem, sementara transaksi berkategori meragukan diarahkan ke verifikasi tambahan yang ramah pengguna.")

    # Tabel 3.3 Decision Support
    p_tbl4_cap = doc.add_paragraph()
    p_tbl4_cap.paragraph_format.space_before = Pt(8)
    p_tbl4_cap.paragraph_format.space_after = Pt(4)
    r_cap4 = p_tbl4_cap.add_run("Tabel 3.3 Kerangka Keputusan Mitigasi Berbasis Skor Risiko")
    r_cap4.bold = False
    r_cap4.font.size = Pt(11)

    dec_data = [
        ("Zona Risiko", "Rentang Skor Matematis", "Kebijakan Tindakan Sistem", "Dampak Operasional bagi Pengguna", "Rasionalitas Ambang Batas"),
        ("Zona Hijau (Risiko Rendah)", "[0, θ_1) di mana θ_1 ≈ 30", "Auto-Approve: Promo otomatis diterapkan langsung tanpa verifikasi tambahan.", "Pengalaman transaksi mulus berlangsung mulus tanpa hambatan.", "Mengoptimalkan retensi pertumbuhan pelanggan sah dengan target FPR <= 2%."),
        ("Zona Kuning (Risiko Sedang)", "[θ_1, θ_2) di mana θ_2 ≈ 70", "Step-Up Verification: Meminta verifikasi OTP sekunder via WhatsApp/SMS.", "Friksi ringan yang wajar guna membuktikan keaslian nomor telepon.", "Mengelola ambiguitas perilaku akun baru tanpa pembatalan sepihak."),
        ("Zona Merah (Risiko Tinggi)", "[θ_2, 100]", "Promotion Denial: Klaim promo ditolak, pesanan dialihkan ke harga normal.", "Subsidi promosi terselamatkan seketika tanpa penonaktifan akun permanen.", "Menjaga efisiensi anggaran dengan batas toleransi risiko pada presisi >= 85%.")
    ]

    tbl_dec = doc.add_table(rows=len(dec_data), cols=5)
    tbl_dec.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_dec.autofit = False
    col_w_dec = [Cm(2.6), Cm(2.4), Cm(4.2), Cm(4.0), Cm(3.8)]
    set_table_borders(tbl_dec)

    for r_idx, row_vals in enumerate(dec_data):
        row = tbl_dec.rows[r_idx]
        is_header = (r_idx == 0)
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_w_dec[c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx in [0, 1]) else WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_runs(p, val, base_size=Pt(9.5) if not is_header else Pt(10), default_bold=is_header or (c_idx == 0))
            if is_header:
                set_cell_background(cell, "E0E0E0")
            elif r_idx == 1:
                set_cell_background(cell, "E2EFDA")
            elif r_idx == 2:
                set_cell_background(cell, "FFF2CC")
            elif r_idx == 3:
                set_cell_background(cell, "FCE4D6")
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)

    p_after_dec = doc.add_paragraph()
    p_after_dec.paragraph_format.space_before = Pt(8)

    add_body_p("Nilai ambang batas θ_1 ≈ 30 dan θ_2 ≈ 70 pada rancangan triase bersifat acuan awal indikatif yang tidak ditentukan secara sembarang. Ambang batas operasional final akan ditetapkan secara empiris pasca-pelatihan model melalui optimasi titik operasi kurva precision-recall serta pertimbangan utilitas biaya bisnis. Ambang bawah θ_1 dirancang untuk menekan angka salah blokir pelanggan sah hingga di bawah 2 persen, sedangkan ambang atas θ_2 dikunci pada tingkat keyakinan tinggi guna mengamankan anggaran subsidi dengan target presisi minimal 85 persen.")

    add_body_p("Sebagai instrumen pendukung keputusan, penelitian ini membangun artefak prototipe dasbor simulasi pemantauan risiko berbasis Python dan pustaka Streamlit. Pengujian prototipe ini dibatasi secara tegas pada evaluasi simulasi luring menggunakan data uji holdout, tanpa melakukan intervensi langsung terhadap infrastruktur peladen produksi platform. Dasbor ini dirancang untuk menyajikan metrik distribusi risiko secara makro, memvisualisasikan fitur dominan sistemik melalui TreeSHAP summary plot, serta menyediakan inspeksi detail transaksi individual melalui waterfall plot. Dengan demikian, analis risiko dapat meninjau alasan matematis di balik pengelompokan sebuah pesanan ke Zona Kuning atau Zona Merah secara transparan. Mekanisme triase mitigasi bertingkat ini diwujudkan melalui antarmuka dasbor pemantauan risiko interaktif yang memadukan skor global dan penjelasan lokal, sebagaimana diilustrasikan pada Gambar 3.3.")

    # GAMBAR 3.3
    add_figure("gambar_3_3_triase_decision_support.png", "Gambar 3.3  Alur Triase Mitigasi Proporsional dan Desain Prototipe Decision Support", width_cm=14.5)

    add_subheading("3.6 Jadwal Rencana Pelaksanaan Penelitian")
    add_body_p("Rangkaian aktivitas penelitian dirancang berlangsung selama enam bulan kalender, mencakup fase konseptualisasi masalah, pengolahan dataset, eksperimen pemodelan XGBoost, hingga penyusunan laporan akhir skripsi dengan rincian jadwal kerja pada Tabel 3.4.")

    # Tabel 3.4 Jadwal Penelitian
    p_tbl5_cap = doc.add_paragraph()
    p_tbl5_cap.paragraph_format.space_before = Pt(8)
    p_tbl5_cap.paragraph_format.space_after = Pt(4)
    r_cap5 = p_tbl5_cap.add_run("Tabel 3.4 Jadwal Rencana Pelaksanaan Penelitian")
    r_cap5.bold = False
    r_cap5.font.size = Pt(11)

    timeline_data = [
        ("No.", "Tahapan Aktivitas Penelitian", "Bln 1", "Bln 2", "Bln 3", "Bln 4", "Bln 5", "Bln 6"),
        ("1", "Identifikasi Fenomena, Masalah Bisnis, & Literatur Primer", "✓", "", "", "", "", ""),
        ("2", "Perancangan Kerangka Sosioteknis & Matriks Celah Riset", "", "✓", "", "", "", ""),
        ("3", "Penyusunan Naskah Proposal & Ujian Seminar Proposal", "", "", "✓", "", "", ""),
        ("4", "Penyiapan Data Sekunder, Audit Label, & Pra-pemrosesan Data", "", "", "", "✓", "", ""),
        ("5", "Eksperimen Pemodelan XGBoost, Penanganan Imbalance, & Tuning", "", "", "", "", "✓", ""),
        ("6", "Kalibrasi Probabilitas (Platt Scaling) & Analisis TreeSHAP", "", "", "", "", "✓", ""),
        ("7", "Perancangan Prototipe Dasbor Triase & Validasi Keputusan", "", "", "", "", "", "✓"),
        ("8", "Penyusunan Laporan Akhir Skripsi & Ujian Pendadaran Sarjana", "", "", "", "", "", "✓")
    ]

    tbl_tl = doc.add_table(rows=len(timeline_data), cols=8)
    tbl_tl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_tl.autofit = False
    col_w_tl = [Cm(1.0), Cm(9.0), Cm(1.1), Cm(1.1), Cm(1.1), Cm(1.1), Cm(1.1), Cm(1.1)]
    set_table_borders(tbl_tl)

    for r_idx, row_vals in enumerate(timeline_data):
        row = tbl_tl.rows[r_idx]
        is_header = (r_idx == 0)
        for c_idx, val in enumerate(row_vals):
            cell = row.cells[c_idx]
            cell.width = col_w_tl[c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if (is_header or c_idx != 1) else WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_runs(p, val, base_size=Pt(9.0) if not is_header else Pt(9.5), default_bold=is_header or (c_idx == 0))
            if is_header:
                set_cell_background(cell, "E0E0E0")
            elif val == "✓":
                set_cell_background(cell, "E2EFDA")
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

    p_after_tl = doc.add_paragraph()
    p_after_tl.paragraph_format.space_before = Pt(8)

    add_subheading("3.7 Etika Penelitian")
    add_body_p("Penelitian ini mematuhi standar integritas akademik dan tata kelola perlindungan data digital secara penuh. Prinsip perlindungan data tanpa informasi identitas pribadi Zero PII ditegakkan dengan mewajibkan seluruh pengenal sensitif, meliputi nama pengguna, nomor telepon aktual, alamat surat elektronik, alamat IP, identitas perangkat, serta rincian jalan alamat pengiriman, telah disamarkan atau dienkripsi satu arah menggunakan algoritma kriptografi SHA-256 sebelum data dimasukkan ke dalam lingkungan pemodelan. Peneliti tidak menyimpan, memproses, maupun mempublikasikan kunci dekripsi data pengenal tersebut.")
    
    add_body_p("Sejalan dengan kebijakan integritas data ilmiah, seluruh tahapan penelitian dilaksanakan dengan menolak segala bentuk rekayasa dataset, manipulasi sepihak label kebenaran dasar, maupun pemalsuan capaian metrik evaluasi eksperimen. Apabila terjadi kendala administratif pada ketersediaan data sekunder industri, peneliti berkomitmen menempuh jalur kontingensi akademik formal secara transparan. Penelitian ini diposisikan secara mutlak untuk tujuan pertahanan dan perlindungan efisiensi sistem informasi, serta tidak mengeksplorasi teknik eksploitasi celah keamanan yang dapat disalahgunakan untuk merugikan ekosistem digital.")

    # ==================== DAFTAR PUSTAKA ====================
    doc.add_page_break()
    add_major_title("DAFTAR PUSTAKA")
    references = [
        "Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. Part I: The causes. *MIS Quarterly*, 1(3), 17–32. https://doi.org/10.2307/248710",
        "Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. CRISP-DM Consortium.",
        "Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '16)* (pp. 785–794). ACM. https://doi.org/10.1145/2939672.2939785",
        "DemandSage, & Riskified. (2024). *The state of policy abuse and promotional fraud in modern e-commerce*. Riskified Research & DemandSage Industry Insights.",
        "Fiarni, C., Gunawan, A. S., & Anthony, I. (2022). Detection system of promotion abuse using similarity and risk scoring methods. *Jurnal Nasional Teknik Elektro dan Teknologi Informasi (JNTETI)*, 11(3), 168–175. https://doi.org/10.22146/jnteti.v11i3.3743",
        "Gupta, A., Shukla, S., Kikan, V., & Kumar, S. (2024). Enhancing fraud detection in credit card transactions using XGBoost and SMOTE: A comparative study. In *2024 IEEE International Conference on Smart Power Control and Renewable Energy (ICSPCRE)* (pp. 1–6). IEEE. https://doi.org/10.1109/icspcre62303.2024.10675080",
        "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105. https://doi.org/10.2307/25148625",
        "Kumar, B. S., Yadav, P. P., & Reddy, M. R. (2024). An intelligent approach to detect and predict online fraud transaction using XGBoost algorithm. *Indonesian Journal of Electrical Engineering and Computer Science (IJEECS)*, 35(3), 1491–1498. https://doi.org/10.11591/ijeecs.v35.i3.pp1491-1498",
        "Leavitt, H. J. (1965). Applied organizational change in industry: Structural, technological and humanistic approaches. In J. G. March (Ed.), *Handbook of Organizations* (pp. 1144–1170). Rand McNally.",
        "Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. In *Advances in Neural Information Processing Systems (NeurIPS 2017)* (Vol. 30, pp. 4765–4774). Curran Associates, Inc.",
        "Niculescu-Mizil, A., & Caruana, R. (2005). Predicting good probabilities with supervised learning. In *Proceedings of the 22nd International Conference on Machine Learning (ICML '05)* (pp. 625–632). ACM. https://doi.org/10.1145/1102351.1102430",
        "Ravelin. (2024). *Global fraud survey: Trends in voucher, return and multi-accounting fraud across on-demand and online retail*. Ravelin Technology Ltd.",
        "Tian, Y., Zhang, X., Liu, C., & Wang, H. (2024). CATeye: Coupled attribute-topology invariance learning for voucher abuse detection. *arXiv preprint arXiv:2409.07062*.",
        "Universitas Negeri Semarang. (2026). *Buku pedoman penyusunan proposal dan skripsi program sarjana fakultas matematika dan ilmu pengetahuan alam*. FMIPA UNNES.",
        "Wen, Z., Fang, Y., Liu, Y., Guo, Y., & Hao, S. (2023). Voucher abuse detection with prompt-based fine-tuning on graph neural networks. In *Proceedings of the 32nd ACM International Conference on Information and Knowledge Management (CIKM '23)* (pp. 4864–4870). ACM. https://doi.org/10.1145/3583780.3615505"
    ]
    for ref in references:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.27)
        p.paragraph_format.first_line_indent = Cm(-1.27)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_formatted_runs(p, ref, base_size=Pt(12))

    # Save document
    doc.save(output_path)
    print(f"Document successfully created at: {output_path}")

if __name__ == "__main__":
    output_docx_path = r"C:\projects\Promoabuse\Proposal_Skripsi_UNNES_2026.docx"
    create_proposal_document(output_docx_path)
