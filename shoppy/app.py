from flask import Flask, render_template, request

app = Flask(__name__)


PRODUCTS = [
    {'name': 'dildo'},
    {'name': 'antirkn'},
    {'name': 'nimbus 2000'},
]


@app.route('/')
def catalog():
    search = request.args.get('q', '')
    products = PRODUCTS
    if search:
        products = [p for p in PRODUCTS if search in p['name']]
    return render_template('catalog.jinja2', products=products, search=search)
