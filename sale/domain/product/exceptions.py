class ProductNameIsInvalid(Exception):
    def __init__(self, message):
        self.message = message

class ProductIdIsInvalid(Exception):
    def __init__(self, message):
        self.message = message