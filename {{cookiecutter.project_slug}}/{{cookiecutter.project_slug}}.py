# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """TODO: Docstring for index.

    :returns: TODO

    """
    return 'OK'

if __name__ == "__main__":
    app.run()
