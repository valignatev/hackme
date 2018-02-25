from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def catalog():
    catalog = [
        {'content': 1},
        {'content': 2},
        {'content': 3},
    ]
    return render_template('catalog.jinja2', catalog=catalog)
