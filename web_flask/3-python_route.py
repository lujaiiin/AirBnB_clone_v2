#!/usr/bin/python3
"""Modules"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello functin"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hhbnb():
    """hhbnb fun"""

    return 'HBNB'


@app.route('/c/<path:text>', strict_slashes=False)
def c_text(text):
    """c_text function"""
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<path:text>', defaults={'text': 'is cool'}, strict_slashes=False)
def py_text(text):
    """python_text function"""
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
