# utils/pdf_utils.py

# import os
# from fpdf import FPDF
# import matplotlib.pyplot as plt
# from datetime import datetime

# # def generate_pos_chart(book_name, pos_data):
# #     os.makedirs("static/charts", exist_ok=True)
# #     chart_path = f"static/charts/{book_name.lower()}_pos_chart.png"
# #     plt.figure(figsize=(10, 6))
# #     plt.bar(pos_data.keys(), pos_data.values(), color='teal')
# #     plt.title(f'POS Tag Frequencies: {book_name}')
# #     plt.xlabel('POS Tags')
# #     plt.ylabel('Frequency')
# #     plt.xticks(rotation=45)
# #     plt.tight_layout()
# #     plt.savefig(chart_path)
# #     plt.close()
# #     return chart_path

# def generate_pos_chart(book_name, pos_data):
#     os.makedirs("static/charts", exist_ok=True)
#     chart_path = f"static/charts/{book_name.lower()}_pos_chart.png"

#     # 🧼 Clean/sanitize to avoid TypeError
#     cleaned_data = {
#         str(k): int(v) for k, v in pos_data.items()
#         if isinstance(v, (int, float)) and not isinstance(v, dict)
#     }

#     if not cleaned_data:
#         raise ValueError("POS data is empty or malformed.")

#     plt.figure(figsize=(10, 6))
#     plt.bar(cleaned_data.keys(), cleaned_data.values(), color='teal')
#     plt.title(f'POS Tag Frequencies: {book_name}')
#     plt.xlabel('POS Tags')
#     plt.ylabel('Frequency')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.savefig(chart_path)
#     plt.close()
#     return chart_path


# def generate_pdf(book_name, pos_data):
#     print("[DEBUG] Starting generate_pdf()")
#     print(f"[DEBUG] Book: {book_name}")
#     print(f"[DEBUG] POS data: {pos_data}")

#     pdf_path = f"pdf/{book_name.lower()}_report.pdf"
#     date_str = datetime.now().strftime("%B %d, %Y")
#     chart_path = generate_pos_chart(book_name, pos_data)
#     logo_path = "static/logos/theta_logo.png"
#     os.makedirs("pdf", exist_ok=True)
#     pdf_path = f"pdf/{book_name.lower()}_report.pdf"
#     doi = f"grapho-stat-report-2025-{book_name.lower()}"

#     # Check if output folder exists
#     print(f"[DEBUG] Saving to path: {pdf_path}")
#     print(f"[DEBUG] Directory exists? {os.path.exists('pdf')}")

#     pdf = FPDF()
#     pdf.add_page()

#     if os.path.exists(logo_path):
#         pdf.image(logo_path, x=80, w=50)
#     pdf.set_font("Arial", "B", 18)
#     pdf.cell(0, 10, f"GraphoStat Report: Stylistic Analysis of {book_name}", ln=True, align='C')
#     pdf.set_font("Arial", "", 14)
#     pdf.cell(0, 10, "A Computational Linguistic Profile", ln=True, align='C')
#     pdf.ln(10)
#     pdf.set_font("Arial", "", 12)
#     pdf.cell(0, 10, f"Date: {date_str}", ln=True, align='C')
#     pdf.cell(0, 10, "Contact: brandonvanderventel@gmail.com", ln=True, align='C')

#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Cite As:", ln=True)
#     pdf.set_font("Arial", "", 12)
#     pdf.multi_cell(0, 10,
#         f"GraphoStat Team (2025). *Stylistic Analysis of {book_name}*. GraphoStat Report Series.\n"
#         f"DOI: {doi}\n"
#         f"Contact: brandonvanderventel@gmail.com"
#     )

#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "Table of Contents", ln=True)
#     pdf.set_font("Arial", "", 12)
#     pdf.cell(0, 10, "1. POS Tag Frequencies", ln=True)

#     pdf.add_page()
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(0, 10, "1. POS Tag Frequencies", ln=True)
#     pdf.set_font("Arial", "", 12)

#     for tag, count in pos_data.items():
#         pdf.cell(0, 10, f"{tag}: {count}", ln=True)

#     if os.path.exists(chart_path):
#         pdf.image(chart_path, x=10, w=180)
#         pdf.ln(10)
#         pdf.multi_cell(0, 10, f"This bar chart represents the distribution of parts of speech in the epistle to {book_name}. "
#                               "It forms the basis for stylistic comparison in later sections.")

#     pdf.output(pdf_path)
#     print("[✓] generate_pdf() from pdf_utils.py is running")
#     print(f"[✓] Saving PDF to: {pdf_path}")

#     return pdf_path

# utils/pdf_utils.py

import os
from fpdf import FPDF
import matplotlib.pyplot as plt
from datetime import datetime


def generate_pos_chart(book_name, pos_data):
    os.makedirs("static/charts", exist_ok=True)
    chart_path = f"static/charts/{book_name.lower()}_pos_chart.png"

    # Clean, sort, and format POS data
    cleaned_data = {
        k.rstrip('-'): int(v)
        for k, v in pos_data.items()
        if isinstance(v, (int, float)) and not isinstance(v, dict)
    }
    sorted_items = sorted(cleaned_data.items())

    if not sorted_items:
        raise ValueError("POS data is empty or malformed.")

    labels, values = zip(*sorted_items)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color='teal')
    # plt.xlabel("POS Tags")
    # plt.ylabel("Frequency")

    # Increase font sizes
    plt.xlabel('POS Tags', fontsize=16)
    plt.ylabel('Frequency', fontsize=16)
    # plt.title('Part-of-Speech Tag Distribution', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # for bar in bars:
    #     yval = bar.get_height()
    #     plt.text(bar.get_x() + bar.get_width() / 2, yval + 30, str(yval), ha='center', va='bottom')

    # Add value labels close to the top of the bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 5,  # 5 = small vertical offset
                f'{int(height)}',
                ha='center', va='bottom', fontsize=12, color='black')  # Adjust fontsize here too

    # Remove the top and right box lines ("spines")
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def generate_noun_chart(book_name, df):
    import matplotlib.pyplot as plt
    from collections import Counter

    os.makedirs("static/charts", exist_ok=True)
    chart_path = f"static/charts/{book_name.lower()}_noun_chart.png"

    # Filter for nouns
    noun_df = df[df['POS'] == 'N-']

    # Count combinations based on positions 4–6 of parsing
    counts = Counter(noun_df['Parsing'].apply(lambda x: x[4:7]))

    if not counts:
        raise ValueError("No valid noun combinations found.")

    # Sort by frequency
    items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    labels, values = zip(*items)

    plt.figure(figsize=(12, 6))
    bars = plt.bar(labels, values, color='darkorange')

    # Label styling
    plt.xlabel('Parsing Combination (Case–Number–Gender)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(fontsize=11, rotation=45)
    plt.yticks(fontsize=12)

    for bar in bars:
        height = bar.get_height()
        if height > 10:
            plt.text(bar.get_x() + bar.get_width() / 2, height - 8,
                     f'{int(height)}', ha='center', va='top', color='white', fontsize=10)
        else:
            plt.text(bar.get_x() + bar.get_width() / 2, height + 3,
                     f'{int(height)}', ha='center', va='bottom', fontsize=10)

    # Clean style
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def generate_pdf(book_name, pos_data):
    print("🛠️ RUNNING UPDATED generate_pdf() from GraphoStat")
    print("[DEBUG] Starting generate_pdf()")
    pdf_path = f"pdf/{book_name.lower()}_report.pdf"
    date_str = datetime.now().strftime("%B %d, %Y")
    chart_path = generate_pos_chart(book_name, pos_data)
    logo_path = "static/logos/theta_logo.png"
    os.makedirs("pdf", exist_ok=True)
    doi = f"grapho-stat-report-2025-{book_name.lower()}"

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

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Cite As:", ln=True)
    pdf.set_font("Arial", "I", 12)
    pdf.multi_cell(0, 10,
        f"GraphoStat Team (2025). Stylistic Analysis of {book_name}. GraphoStat Report Series.")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"DOI: {doi}", ln=True)
    pdf.cell(0, 10, "Data Source: https://github.com/morphgnt/sblgnt", ln=True)

    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Table of Contents", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "1. POS Tag Frequencies", ln=True)
    pdf.cell(0, 10, "2. Noun Parsing Combinations", ln=True)


    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "1. POS Tag Frequencies", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10,
        "This section provides a quantitative overview of the frequency of parts of speech in "
        f"the epistle to {book_name}. The POS codes are as follows:"
    )

    # pdf.ln(5)
    # pdf.set_font("Arial", "B", 12)
    # pdf.cell(0, 10, "Legend for POS Tags:", ln=True)

    pdf.set_font("Arial", "", 11)
    legend_text = (
        "- A: adjective\n"
        "- C: conjunction\n"
        "- D: adverb\n"
        "- I: interjection\n"
        "- N: noun\n"
        "- P: preposition\n"
        "- RA: article\n"
        "- RD: demonstrative pronoun\n"
        "- RI: interrogative/indefinite pronoun\n"
        "- RP: personal pronoun\n"
        "- RR: relative pronoun\n"
        "- V: verb\n"
        "- X: particle"
    )

    pdf.multi_cell(0, 8, legend_text)
    if os.path.exists(chart_path):
        pdf.image(chart_path, x=10, w=180)

        # Load CSV for noun analysis
    csv_path = f"data/{book_name_to_filename[book_name]}"  # you must define this mapping
    df = pd.read_csv(csv_path)

    noun_chart_path = generate_noun_chart(book_name, df)

    # Add Section 2: Noun Parsing Combinations
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "2. Noun Parsing Combinations", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10,
        "This section displays all unique parsing combinations of nouns in the epistle to "
        f"{book_name}. Each combination encodes case, number, and gender."
    )

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8,
        "Parsing Code:\n"
        "- Case: N=nominative, G=genitive, D=dative, A=accusative, V=vocative\n"
        "- Number: S=singular, P=plural\n"
        "- Gender: M=masculine, F=feminine, N=neuter\n"
        "Example: NPM = Nominative Plural Masculine"
    )

    if os.path.exists(noun_chart_path):
        pdf.image(noun_chart_path, x=10, w=180)


    pdf.output(pdf_path)
    print("[✓] generate_pdf() from pdf_utils.py is running")
    print(f"[✓] Saving PDF to: {pdf_path}")
    return pdf_path
