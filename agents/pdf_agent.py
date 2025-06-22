# agents/pdf_agent.py

from utils.pdf_utils import generate_pdf

class PDFGenerationAgent:
    @staticmethod
    def run(book, pos_data):
        pdf_path = generate_pdf(book, pos_data)
        print(f"[DEBUG] PDF created at: {pdf_path}")
        return pdf_path
