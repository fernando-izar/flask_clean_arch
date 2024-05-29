import sys
from .models import Sale
from sale.application.sale.sale_dto import SaleDto
from .models import db
from sale.application.sale.sale_storage import SaleStorage

sys.path.append("..")
sys.path.append("../..")


class SaleRepository(SaleStorage):
    def __init__(self):
        self.db = db

    def save_sale(self, sale_dto: SaleDto):
        pass

    def _model_to_dto(self, sale: Sale):
        return SaleDto(
            id=sale.id,
            date=sale.date,
            product_dto=sale.product,
            quantity=sale.quantity,
        )

    def get_all_sales(self, sale_id):
        sales = Sale.query.all()
        return [self._model_to_dto(sale) for sale in sales]
