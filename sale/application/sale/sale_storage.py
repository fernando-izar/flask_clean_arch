from abc import ABC, abstractmethod
from .sale_dto import SaleDto


class SaleStorage(ABC):

    @abstractmethod
    def save_sale(self, sale_dto: SaleDto):
        pass
