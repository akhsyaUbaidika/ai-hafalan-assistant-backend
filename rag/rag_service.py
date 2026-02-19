from openai import OpenAI
from rag.chroma_client import collection

client = OpenAI()

def embed_query(query: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    return response.data[0].embedding


def search_knowledge(query: str, k: int = 3):
    query_embedding = embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    docs = results.get("documents", [[]])[0]
    return "\n".join(docs)
