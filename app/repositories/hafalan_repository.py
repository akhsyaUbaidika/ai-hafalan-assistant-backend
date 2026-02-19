from app.core.firebase import db

class HafalanRepository:

    @staticmethod
    def get_hafalan_by_periode(bulan: str, tahun: str):
        docs = (
            db.collection("hafalan_harian_santri")
            .where("bulan", "==", bulan)
            .where("tahun", "==", tahun)
            .stream()
        )
        return [doc.to_dict() for doc in docs]
