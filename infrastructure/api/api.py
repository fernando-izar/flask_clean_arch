from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.app_context().push()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def hello_world():
    return {'message': 'Hello, World!'}	

@app.route('/products')	
def get_products():
    products = Product.query.all()
    return {'products': [product.name for product in products]}