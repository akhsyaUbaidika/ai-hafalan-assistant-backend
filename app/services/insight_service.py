from app.services.data_service import DataService
from app.core.openai_client import client
from app.core.config import settings

MODEL = settings.model_name

# simple in-memory cache
insight_cache = {}


class InsightService:

    @staticmethod
    def generate_monthly_insight(bulan: str, tahun: str):

        # ========= CACHE CHECK =========
        cache_key = f"{bulan}-{tahun}"
        if cache_key in insight_cache:
            return insight_cache[cache_key]

        # ========= AMBIL DATA =========
        data = DataService.get_hafalan_by_month(bulan, tahun)

        if len(data) == 0:
            return "Tidak ada data pada bulan tersebut."

        # ========= RINGKAS DATA =========
        ringkasan = []
        for item in data[:50]:  # batasi biar hemat token
            ringkasan.append(
                f"{item['nama']} | hadir:{item['kehadiran']} | "
                f"setoran:{item['kelancaran_setoran']} | "
                f"murajaah:{item['kelancaran_murojaah']} | "
                f"tadarus:{item['kelancaran_tadarus']}"
            )

        data_text = "\n".join(ringkasan)

        # ========= PROMPT AI =========
        system_prompt = f"""
Kamu adalah analis pendidikan di lembaga tahfiz Al-Qur'an.

Buat laporan insight performa santri bulanan berdasarkan data berikut:

{data_text}

Format laporan:
1. Ringkasan performa umum
2. Santri paling konsisten
3. Santri yang perlu perhatian
4. Rekomendasi peningkatan
"""

        # ========= CALL OPENAI =========
        try:
            response = client.responses.create(
                model=MODEL,
                input=system_prompt,
                temperature=0.4
            )

            result = response.output[0].content[0].text

            # simpan ke cache
            insight_cache[cache_key] = result

            return result

        except Exception as e:
            return "Terjadi kesalahan saat membuat insight AI."
