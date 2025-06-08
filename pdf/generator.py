def generate_pdf(book: str, result: dict, explanation: str) -> str:
    filename = f"{book.lower()}_report.pdf"
    with open(filename, "w") as f:
        f.write("Placeholder PDF content.\n")
        f.write("Explanation:\n")
        f.write(explanation)
    return filename
