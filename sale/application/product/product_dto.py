from sale.domain.product.entities import Product


class ProductDto(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def _to_domain(self):
        return Product(
            id=self.id,
            name=self.name,
        )
