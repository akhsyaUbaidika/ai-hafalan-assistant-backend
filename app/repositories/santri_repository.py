from app.data_providers.provider_factory import get_provider

provider = get_provider()

class SantriRepository:

    @staticmethod
    def get_all_santri():
        return provider.get_all_santri()
