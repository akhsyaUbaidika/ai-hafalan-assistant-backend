from abc import ABC, abstractmethod

class BaseDataProvider(ABC):

    @abstractmethod
    def get_all_santri(self):
        pass

    @abstractmethod
    def get_hafalan_by_periode(self, bulan: str, tahun: str):
        pass
