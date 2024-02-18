#!/usr/bin/python3
"""Modules"""
from flask import Flask, render_template_string
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of all State objects."""
    states = storage.all(State).order_by(State.name).all()
    states_html = ''.join([f'<li>{state.id}: <b>{state.name}</b></li>' for state in states])
    return render_template_string(f'<html><body><h1>States</h1><ul>{states_html}</ul></body></html>')


@app.teardown_appcontext
def close_session(exception=None):
    """Close the storage after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
