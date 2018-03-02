from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.exceptions import abort

app = Flask(__name__)
app.secret_key = 'lol_secret'
app.config['SESSION_COOKIE_HTTPONLY'] = False


USERS = [
    {'id': 1, 'username': 'root', 'password': '123', 'role': 'admin'},
    {'id': 2, 'username': 'alice', 'password': 'poib', 'role': 'user'},
]


CARDS = [
    {'cvc': '123', 'number': '4276 7000 5555 5555'},
    {'cvc': '124', 'number': '4444 4444 4444 4444'},
    {'cvc': '543', 'number': '4242 4242 4242 4242'},
]


PRODUCTS = [
    {'name': '1080ti', 'id': 1, 'price': 123.11},
    {'name': 'antirkn', 'id': 2, 'price': 666.66},
    {'name': 'nimbus 2000', 'id': 3, 'price': 399},
]

REVIEWS = [
    {'id': 1, 'author': 'Vasya', 'text': 'This is awesome', 'product_id': 1},
    {'id': 2, 'author': 'Lesha', 'text': 'Want moar!', 'product_id': 1},
    {'id': 3, 'author': 'Peter', 'text': 'UR MOM', 'product_id': 3},
    {'id': 4, 'author': 'Lesha', 'text': 'kill me please', 'product_id': 3},
]


@app.route('/')
def catalog():
    search = request.args.get('q', '')
    products = PRODUCTS
    if search:
        products = [p for p in PRODUCTS if search in p['name']]
    return render_template(
        'catalog.jinja2',
        products=products,
        search=search,
        user=session.get('user', {}),
    )


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
    return render_template(
        'product.jinja2',
        product=product,
        reviews=reviews,
        user=session.get('user', {}),
    )


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.jinja2', user=session.get('user', {}))
    login = request.form['login']
    password = request.form['password']
    try:
        user = [
            u for u in USERS
            if u['username'] == login and u['password'] == password
        ][0]
    except IndexError:
        return render_template(
            'login.jinja2',
            error='Login or password is incorrect',
            user=session.get('user', {}),
        )
    session['user'] = user
    return redirect(url_for('catalog'))


@app.route('/logout/')
def logout():
    session.pop('user')
    return redirect(url_for('catalog'))


@app.route('/admin/')
def admin():
    try:
        user = session['user']
    except KeyError:
        abort(404)
    if user['role'] == 'admin':
        return render_template(
            'admin.jinja2',
            users=USERS,
            cards=CARDS,
            user=user,
        )
    abort(404)
