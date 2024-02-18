#!/usr/bin/python3
"""Modules"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello function"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hhbnb():
    """hhbnb function"""
    return 'HBNB'

@app.route('/c/<path:text>', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/c/', strict_slashes=False)
def c_text(text):
    """c_text function"""
    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/<path:text>', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text):
    """python_text function"""
    text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """number function"""
    return f'{n} is a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

