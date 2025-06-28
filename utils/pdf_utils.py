# utils/pdf_utils.py

import os
from fpdf import FPDF
import matplotlib.pyplot as plt
from datetime import datetime

# def generate_pos_chart(book_name, pos_data):
#     os.makedirs("static/charts", exist_ok=True)
#     chart_path = f"static/charts/{book_name.lower()}_pos_chart.png"
#     plt.figure(figsize=(10, 6))
#     plt.bar(pos_data.keys(), pos_data.values(), color='teal')
#     plt.title(f'POS Tag Frequencies: {book_name}')
#     plt.xlabel('POS Tags')
#     plt.ylabel('Frequency')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.savefig(chart_path)
#     plt.close()
#     return chart_path

def generate_pos_chart(book_name, pos_data):
    os.makedirs("static/charts", exist_ok=True)
    chart_path = f"static/charts/{book_name.lower()}_pos_chart.png"

    # 🧼 Clean/sanitize to avoid TypeError
    cleaned_data = {
        str(k): int(v) for k, v in pos_data.items()
        if isinstance(v, (int, float)) and not isinstance(v, dict)
    }

    if not cleaned_data:
        raise ValueError("POS data is empty or malformed.")

    plt.figure(figsize=(10, 6))
    plt.bar(cleaned_data.keys(), cleaned_data.values(), color='teal')
    plt.title(f'POS Tag Frequencies: {book_name}')
    plt.xlabel('POS Tags')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path


def generate_pdf(book_name, pos_data):
    print("[DEBUG] Starting generate_pdf()")
    print(f"[DEBUG] Book: {book_name}")
    print(f"[DEBUG] POS data: {pos_data}")

    pdf_path = f"pdf/{book_name.lower()}_report.pdf"
    date_str = datetime.now().strftime("%B %d, %Y")
    chart_path = generate_pos_chart(book_name, pos_data)
    logo_path = "static/logos/theta_logo.png"
    os.makedirs("pdf", exist_ok=True)
    pdf_path = f"pdf/{book_name.lower()}_report.pdf"
    doi = f"grapho-stat-report-2025-{book_name.lower()}"

    # Check if output folder exists
    print(f"[DEBUG] Saving to path: {pdf_path}")
    print(f"[DEBUG] Directory exists? {os.path.exists('pdf')}")

    pdf = FPDF()
    pdf.add_page()

    if os.path.exists(logo_path):
        pdf.image(logo_path, x=80, w=50)
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, f"GraphoStat Report: Stylistic Analysis of {book_name}", ln=True, align='C')
    pdf.set_font("Arial", "", 14)
    pdf.cell(0, 10, "A Computational Linguistic Profile", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Date: {date_str}", ln=True, align='C')
    pdf.cell(0, 10, "Contact: brandonvanderventel@gmail.com", ln=True, align='C')

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Cite As:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10,
        f"GraphoStat Team (2025). *Stylistic Analysis of {book_name}*. GraphoStat Report Series.\n"
        f"DOI: {doi}\n"
        f"Contact: brandonvanderventel@gmail.com"
    )

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Table of Contents", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "1. POS Tag Frequencies", ln=True)

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "1. POS Tag Frequencies", ln=True)
    pdf.set_font("Arial", "", 12)

    for tag, count in pos_data.items():
        pdf.cell(0, 10, f"{tag}: {count}", ln=True)

    if os.path.exists(chart_path):
        pdf.image(chart_path, x=10, w=180)
        pdf.ln(10)
        pdf.multi_cell(0, 10, f"This bar chart represents the distribution of parts of speech in the epistle to {book_name}. "
                              "It forms the basis for stylistic comparison in later sections.")

    pdf.output(pdf_path)
    print("[✓] generate_pdf() from pdf_utils.py is running")
    print(f"[✓] Saving PDF to: {pdf_path}")

    return pdf_path
