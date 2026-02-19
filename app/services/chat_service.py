from app.repositories.hafalan_repository import HafalanRepository
from app.core.openai_client import client
from rag.rag_service import search_knowledge

import os

MODEL = os.getenv("MODEL_NAME")

class ChatService:

    @staticmethod
    def ask_ai(message: str):

        # 1. Ambil data hafalan Mei 2025 (sementara hardcoded MVP)
        data = HafalanRepository.get_hafalan_by_periode("Mei", "2025")

        # 2. Batasi data biar tidak jebol token
        data = data[:50]

        # 3. Ubah data jadi context text
        context_lines = []
        for d in data:
            line = (
                f"{d['nama']} | hadir:{d['kehadiran']} | "
                f"setoran:{d['kelancaran_setoran']} | "
                f"murojaah:{d['kelancaran_murojaah']} | "
                f"tadarus:{d['kelancaran_tadarus']}"
            )
            context_lines.append(line)

        context_text = "\n".join(context_lines)

        # 4. System prompt
        knowledge_text = search_knowledge(message)

        system_prompt = f"""
Kamu adalah AI Hafalan Assistant.

Gunakan dua sumber berikut untuk menjawab:

1) KNOWLEDGE BASE (aturan & interpretasi)
{knowledge_text}

2) DATA HAFALAN SANTRI
{context_text}

Jawab dengan bahasa Indonesia yang jelas dan informatif.
"""


        # 5. Call OpenAI
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content
