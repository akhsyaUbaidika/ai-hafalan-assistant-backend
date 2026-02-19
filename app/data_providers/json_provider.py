import json
from pathlib import Path
from app.data_providers.base_provider import BaseDataProvider

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SANTRI_FILE = BASE_DIR / "santri_master.json"
HAFALAN_FILE = BASE_DIR / "hafalan_harian_santri_v2.json"

class JsonDataProvider(BaseDataProvider):

    def get_all_santri(self):
        with open(SANTRI_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_hafalan_by_periode(self, bulan: str, tahun: str):
        with open(HAFALAN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [
            item for item in data
            if item.get("bulan") == bulan and item.get("tahun") == tahun
        ]
