import os
from app.data_providers.json_provider import JsonDataProvider
from app.data_providers.firebase_provider import FirebaseDataProvider

def get_provider():
    source = os.getenv("DATA_SOURCE", "json").lower()

    if source == "firebase":
        return FirebaseDataProvider()

    return JsonDataProvider()
