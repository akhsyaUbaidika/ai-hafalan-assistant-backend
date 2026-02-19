import chromadb

def get_chroma_client():
    client = chromadb.Client(
        chromadb.config.Settings(
            persist_directory="chroma_db",
            anonymized_telemetry=False
        )
    )
    return client

client = get_chroma_client()
collection = client.get_or_create_collection(name="knowledge_base")
