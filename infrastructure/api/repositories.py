import sys

sys.path.append("..")
sys.path.append("../..")
from .models import Sale, Product
from sale.application.sale.sale_dto import SaleDto
from .models import db
from sale.application.sale.sale_storage import SaleStorage
from sale.application.product.produtc_storage import ProductStorage
from sale.application.product.product_dto import ProductDto


class SaleRepository(SaleStorage):
    def __init__(self):
        self.db = db

    def save_sale(self, sale_dto: SaleDto):
        pass

    def _model_to_dto(self, sale: Sale):
        return SaleDto(
            id=sale.id,
            date=sale.date,
            product_dto=sale.product_id,
            quantity=sale.quantity,
        )

    def get_all_sales(self) -> list[SaleDto]:
        sales = Sale.query.all()
        return [self._model_to_dto(sale) for sale in sales]


class ProductRepository(ProductStorage):
    def __init__(self):
        self.db = db

    def save_product(self, product_dto: ProductDto):
        pass

    def _model_to_dto(self, product):
        return ProductDto(
            id=product.id,
            name=product.name,
        )

    def get_all_products(self):
        products = Product.query.all()
        return [self._model_to_dto(product) for product in products]
