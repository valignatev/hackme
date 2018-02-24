import os
from string import Template

from flask import Flask

app = Flask(__name__)
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


@app.route('/')
def catalog():
    print(TEMPLATE_DIR)
    with open(f'{TEMPLATE_DIR}/catalog.html') as f:
        template = Template(f.read())
    return template.substitute(content='Sup XSS')
