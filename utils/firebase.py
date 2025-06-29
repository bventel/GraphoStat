import os
import json
import firebase_admin
from firebase_admin import credentials, storage

# Init only once
if not firebase_admin._apps:
    # Load JSON string from env
    firebase_json = os.environ.get("FIREBASE_KEY_JSON")
    if not firebase_json:
        raise ValueError("FIREBASE_KEY_JSON not set in environment variables.")

    cert_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cert_dict)

    # firebase_admin.initialize_app(cred, {
    #     "storageBucket": "digitalproducts-97155.firebasestorage.app"
    # })

    # firebase_admin.initialize_app(cred, {
    #     "storageBucket": "digitalproducts-97155.appspot.com"
    # })

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
