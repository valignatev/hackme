from flask import Flask, render_template, request
from werkzeug.exceptions import abort

app = Flask(__name__)


PRODUCTS = [
    {'name': 'dildo', 'id': 1},
    {'name': 'antirkn', 'id': 2},
    {'name': 'nimbus 2000', 'id': 3},
]


@app.route('/')
def catalog():
    search = request.args.get('q', '')
    products = PRODUCTS
    if search:
        products = [p for p in PRODUCTS if search in p['name']]
    return render_template('catalog.jinja2', products=products, search=search)


@app.route('/product/<int:product_id>')
def product(product_id):
    try:
        product = [p for p in PRODUCTS if p['id'] == product_id][0]
    except IndexError:
        abort(404)
    return render_template('product.jinja2', product=product)
