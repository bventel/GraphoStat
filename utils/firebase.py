import firebase_admin
from firebase_admin import credentials, storage

# Init only once
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred, {
        "storageBucket": "digitalproducts-97155.appspot.com"
    })

def check_if_pdf_exists(book: str) -> str | None:
    bucket = storage.bucket()
    blob = bucket.blob(f"reports/{book.lower()}.pdf")
    if blob.exists():
        blob.make_public()
        return blob.public_url
    return None

def upload_pdf_to_firestore(book: str, local_path: str) -> str:
    bucket = storage.bucket()
    blob = bucket.blob(f"reports/{book.lower()}.pdf")
    blob.upload_from_filename(local_path)
    blob.make_public()
    return blob.public_url
