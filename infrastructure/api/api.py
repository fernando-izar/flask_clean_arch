from flask import Flask
from .models import db
from .models import Product
from .repositories import SaleRepository, ProductRepository
from sale.application.sale.sale_manager import SaleManager
from sale.application.product.product_manager import ProductManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
app.app_context().push()
db.create_all()


@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.route("/products")
def get_products():
    repository = ProductRepository()
    manager = ProductManager(repository)
    products = manager.get_products()

    return {"products": [product.__dict__ for product in products]}


@app.route("/sales")
def get_sales():
    repository = SaleRepository()
    manager = SaleManager(repository)
    sales = manager.get_sales()

    return {"sales": [sale.__dict__ for sale in sales]}
