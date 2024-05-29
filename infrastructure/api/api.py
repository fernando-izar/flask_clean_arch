from flask import Flask
from .models import db
from .models import Product
from .repositories import SaleRepository
from sale.application.sale.sale_manager import SaleManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
app.app_context().push()
# db.create_all()


@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.route("/products")
def get_products():
    products = Product.query.all()
    return {"products": [product.name for product in products]}


@app.route("/sales")
def get_sales():
    repository = SaleRepository()
    manager = SaleManager(repository)
