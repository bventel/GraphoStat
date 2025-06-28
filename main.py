import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

from agents.pos_distribution import POSDistributionAgent
from agents.pdf_agent import PDFGenerationAgent

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    book = data.get("book")  # Expecting 'Romans', 'Matthew', etc.

    if not book:
        return jsonify({"error": "Missing 'book' in request."}), 400

    # 🔍 Run the POS Distribution Agent
    metrics = POSDistributionAgent.run(book)

    print("[DEBUG] Metrics returned by POSDistributionAgent:")
    print(metrics)

    pdf_path = PDFGenerationAgent.run(book, metrics)
    print("pdf_path: ", pdf_path)

    pdf_url = upload_pdf_to_firestore(book, pdf_path)

    if "error" in metrics:
        return jsonify({"error": metrics["error"]}), 500

    return jsonify({
    "book": book,
    "metrics": metrics,
    "pdf_url": pdf_url,
    "source": "firebase"
})


@app.route("/download_pdf/<book>")
def download_pdf(book):
    pdf_path = f"pdf/{book.lower()}_report.pdf"
    if not os.path.exists(pdf_path):
        return jsonify({"error": "PDF not found"}), 404
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
