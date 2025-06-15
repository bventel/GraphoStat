import pandas as pd

class POSDistributionAgent:
    @staticmethod
    def run(book_filename: str) -> dict:
        try:
            df = pd.read_csv(f"data/{book_filename}.csv")  # e.g. 'Romans.csv'
            pos_counts = df["POS"].value_counts().to_dict()
            return {"pos_distribution": pos_counts}
        except Exception as e:
            return {"error": str(e)}
