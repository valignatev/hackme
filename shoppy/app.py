from operator import itemgetter

from flask import Flask, render_template, request
from werkzeug.exceptions import abort

app = Flask(__name__)


PRODUCTS = [
    {'name': 'dildo', 'id': 1, 'price': 123.11},
    {'name': 'antirkn', 'id': 2, 'price': 666.66},
    {'name': 'nimbus 2000', 'id': 3, 'price': 399},
]

REVIEWS = [
    {'id': 1, 'author': 'Vasya', 'text': 'This is shit', 'product_id': 1},
    {'id': 2, 'author': 'Lesha', 'text': 'This is shit', 'product_id': 1},
    {'id': 3, 'author': 'Peter', 'text': 'This is shit', 'product_id': 3},
    {'id': 4, 'author': 'Lesha', 'text': 'This is shit', 'product_id': 3},
]


@app.route('/')
def catalog():
    search = request.args.get('q', '')
    products = PRODUCTS
    if search:
        products = [p for p in PRODUCTS if search in p['name']]
    return render_template('catalog.jinja2', products=products, search=search)


@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    try:
        product = [p for p in PRODUCTS if p['id'] == product_id][0]
    except IndexError:
        abort(404)
    if request.method == 'POST':
        last_review_id = REVIEWS[-1]['id']
        REVIEWS.append(
            {
                'author': request.form['author'],
                'text': request.form['review'],
                'id': last_review_id + 1,
                'product_id': product_id,
            },
        )
    reviews = [r for r in REVIEWS if r['product_id'] == product_id]
    return render_template('product.jinja2', product=product, reviews=reviews)
