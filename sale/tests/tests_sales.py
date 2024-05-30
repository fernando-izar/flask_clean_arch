import unittest
from datetime import datetime
import sys

sys.path.append("..")
sys.path.append("../..")
from sale.domain.sale.entities import Sale
from sale.application.sale.sale_dto import SaleDto
from sale.domain.sale.exceptions import SaleDateIsInvalid
from sale.domain.product.entities import Product
from sale.application.product.product_dto import ProductDto
from sale.application.sale.sale_manager import SaleManager


class SaleTests(unittest.TestCase):

    def test_sale_date_is_invalid(self):
        sale = Sale(id=1, date=None, product=None, quantity=1)

        with self.assertRaises(SaleDateIsInvalid) as ex:
            sale.is_valid()

        exception = ex.exception

        self.assertEqual(exception.message, "Sale date is invalid")

    def test_sale_quantity_is_invalid(self):
        sale = Sale(id=1, date=datetime.now(), product=None, quantity=0)

        with self.assertRaises(Exception) as ex:
            sale.is_valid()

        exception = ex.exception

        self.assertEqual(exception.message, "Sale quantity is invalid")

    def test_sale_create(self):
        id = 1
        date = datetime.now()
        product_dto = ProductDto(id=1, name="Product 1")
        quantity = 1
        sale_dto = SaleDto(
            id=id,
            date=date,
            product_dto=product_dto,
            quantity=quantity,
        )
        manager = SaleManager()
        res = manager.create_new_sale(sale_dto)
        self.assertEqual(res, "save")


if __name__ == "__main__":
    unittest.main()
