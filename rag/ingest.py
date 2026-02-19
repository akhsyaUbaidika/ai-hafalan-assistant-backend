from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI
from rag.chroma_client import collection


client = OpenAI()

KNOWLEDGE_FOLDER = "knowledge"

def read_files():
    docs = []
    for filename in os.listdir(KNOWLEDGE_FOLDER):
        if filename.endswith(".txt"):
            path = os.path.join(KNOWLEDGE_FOLDER, filename)
            with open(path, "r", encoding="utf-8") as f:
                docs.append((filename, f.read()))
    return docs

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def embed(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def run_ingestion():
    docs = read_files()

    for filename, content in docs:
        chunks = chunk_text(content)

        for i, chunk in enumerate(chunks):
            emb = embed(chunk)

            collection.add(
                ids=[f"{filename}_{i}"],
                documents=[chunk],
                embeddings=[emb],
                metadatas=[{"source": filename}]
            )

    print("INGESTION DONE")

if __name__ == "__main__":
    run_ingestion()
