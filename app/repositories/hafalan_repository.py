from app.data_providers.provider_factory import get_provider

provider = get_provider()

class HafalanRepository:

    @staticmethod
    def get_hafalan_by_periode(bulan: str, tahun: str):
        return provider.get_hafalan_by_periode(bulan, tahun)
