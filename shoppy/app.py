from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def catalog():
    return render_template('catalog.jinja2', content='Sup XSS')
