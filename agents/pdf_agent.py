# agents/pdf_agent.py

from utils.pdf_utils import generate_pdf

class PDFGenerationAgent:
    @staticmethod
    def run(book, metrics):
        pos_data = metrics.get("pos_distribution", metrics)  # fallback for direct dict
        pdf_path = generate_pdf(book, pos_data)
        return pdf_path
