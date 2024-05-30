from sale.domain.product.exceptions import ProductNameIsInvalid, ProductIdIsInvalid

class Product(object):
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def is_valid(self):
        if self.name is None or self.name == "":
            raise ProductNameIsInvalid("Product name is invalid")
        if self.id is None or self.id == "" or self.id <= 0:
            raise ProductIdIsInvalid("Product id is invalid")
        
        return True