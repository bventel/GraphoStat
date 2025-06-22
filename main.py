# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend access

# @app.route("/analyze", methods=["POST"])
# def analyze():
#     data = request.get_json()
#     book = data.get("book")

#     if not book:
#         return jsonify({"error": "Missing 'book' in request."}), 400

#     print(f"[Agent Trigger] Book selected for analysis: {book}")

#     dummy_metrics = {
#         "word_count": 5123,
#         "verb_ratio": 0.34,
#         "hapax_legomena": 203,
#         "imperative_density": 0.071
#     }

#     response = {
#         "book": book,
#         "metrics": dummy_metrics,
#         "pdf_url": f"https://example.com/reports/{book.lower()}.pdf"
#     }

#     return jsonify(response), 200

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))

# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from utils.firebase import check_if_pdf_exists, upload_pdf_to_firestore
# from agents.pos_distribution import POSDistributionAgent
# from utils.llm import interpret_metric
# from pdf.generator import generate_pdf

# app = Flask(__name__)
# CORS(app)  # Enable CORS for frontend access

# @app.route("/analyze", methods=["POST"])
# def analyze():
#     data = request.get_json()
#     book = data.get("book")

#     if not book:
#         return jsonify({"error": "Missing 'book' in request."}), 400

#     # ✅ Check Firestore first
#     cached_url = check_if_pdf_exists(book)
#     if cached_url:
#         return jsonify({"book": book, "pdf_url": cached_url, "source": "cache"}), 200

#     # ✅ Load CSV (assumes naming convention)
#     df = pd.read_csv(f"data/{book}.csv")  # e.g., 66-Ro-morphgnt.csv → romans.csv

#     # ✅ Placeholder until agents are connected
#     dummy_metrics = {
#         "word_count": len(df),
#         "pos_counts": df['morph'].value_counts().to_dict()  # placeholder
#     }

#     # ✅ Placeholder PDF
#     dummy_path = f"{book.lower()}_report.pdf"
#     with open(dummy_path, "w") as f:
#         f.write("This is a placeholder PDF.\n")

#     # ✅ Upload to Firebase
#     pdf_url = upload_pdf_to_firestore(book, dummy_path)

#     return jsonify({
#         "book": book,
#         "metrics": dummy_metrics,
#         "pdf_url": pdf_url,
#         "source": "new"
#     }), 200

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

    if "error" in metrics:
        return jsonify({"error": metrics["error"]}), 500

    return jsonify({
    "book": book,
    "metrics": metrics,
    "pdf_url": f"https://graphostat-api.onrender.com/download_pdf/{book.lower()}",
    "source": "live"
})


@app.route("/download_pdf/<book>")
def download_pdf(book):
    pdf_path = f"pdf/{book.lower()}_report.pdf"
    if not os.path.exists(pdf_path):
        return jsonify({"error": "PDF not found"}), 404
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
