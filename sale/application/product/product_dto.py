from sale.domain.product.entities import Product


class ProductDto(object):

    def __init__(self, name):
        self.name = name

    def _to_domain(self):
        return Product(
            name=self.name,
        )

    def _to_dto(self, product: Product):
        return ProductDto(
            name=product.name,
        )
