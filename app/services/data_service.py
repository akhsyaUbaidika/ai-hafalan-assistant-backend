import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SANTRI_FILE = BASE_DIR / "santri_master.json"
HAFALAN_FILE = BASE_DIR / "hafalan_harian_santri_v2.json"


class DataService:

    @staticmethod
    def load_santri():
        with open(SANTRI_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def load_hafalan():
        with open(HAFALAN_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def get_hafalan_by_month(bulan: str, tahun: str):
        data = DataService.load_hafalan()
        hasil = []

        for item in data:
            if item.get("bulan") == bulan and item.get("tahun") == tahun:
                hasil.append(item)

        return hasil
