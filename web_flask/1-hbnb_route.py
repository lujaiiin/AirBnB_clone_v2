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

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
