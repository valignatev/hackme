# Shoppy - the very bugged ecommerse from poib 2018 talk.

![Thumbnail](https://github.com/valignatev/hackme/blob/master/thumbnail.jpg)

Recorded talk is [here (click)](https://www.youtube.com/watch?v=iC8blfEAcMM)

## Run it yourself

```bash
$ git clone git@github.com:valignatev/hackme.git
$ cd hackme
$ pipenv install --three # you should have python3 and pipenv installed
$ cd shoppy
$ FLASK_APP=app.py FLASK_DEBUG=1 flask run # to run main store app
$ FLASK_APP=steal.py FLASK_DEBUG=1 flask run --host=127.0.0.1 --port=5010 # to run cookie stealing app
$ pytest --driver Firefox  # to run tests, should have Firefox and geckodriver somewhere in PATH
```

All presentation related stuff is in talks dir, if it helps

(c) hujak, hujak i v production 3018
