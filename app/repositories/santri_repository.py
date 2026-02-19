from app.core.firebase import db

class SantriRepository:

    @staticmethod
    def get_all_santri():
        docs = db.collection("santri_master").stream()
        return [doc.to_dict() for doc in docs]
