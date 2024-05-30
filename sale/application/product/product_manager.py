from sale.application.product.produtc_storage import ProductDto, ProductStorage


class ProductManager:
    storage: ProductStorage

    def __init__(self, storage: ProductStorage) -> None:
        self.storage = storage

    def get_products(self):
        return self.storage.get_all_products()
