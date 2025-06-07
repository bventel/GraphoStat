import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    book = data.get("book")

    if not book:
        return jsonify({"error": "Missing 'book' in request."}), 400

    print(f"[Agent Trigger] Book selected for analysis: {book}")

    dummy_metrics = {
        "word_count": 5123,
        "verb_ratio": 0.34,
        "hapax_legomena": 203,
        "imperative_density": 0.071
    }

    response = {
        "book": book,
        "metrics": dummy_metrics,
        "pdf_url": f"https://example.com/reports/{book.lower()}.pdf"
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
