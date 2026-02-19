import firebase_admin
from firebase_admin import credentials, firestore
from app.data_providers.base_provider import BaseDataProvider


class FirebaseDataProvider(BaseDataProvider):

    def __init__(self):
        self.db = self.init_firestore()

    def init_firestore(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate("firebase_key.json")
            firebase_admin.initialize_app(cred)

        return firestore.client()

    def get_all_santri(self):
        docs = self.db.collection("santri_master").stream()
        return [doc.to_dict() for doc in docs]

    def get_hafalan_by_periode(self, bulan: str, tahun: str):
        docs = (
            self.db.collection("hafalan_harian_santri")
            .where("bulan", "==", bulan)
            .where("tahun", "==", tahun)
            .stream()
        )
        return [doc.to_dict() for doc in docs]
