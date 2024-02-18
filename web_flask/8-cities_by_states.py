#!/usr/bin/python3
"""Modules"""
from flask import Flask, render_template_string
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a list of all State objects and their cities."""
    states = storage.all(State).order_by(State.name).all()
    states_html = ''
    for state in states:
        cities = state.cities if isinstance(storage, DBStorage) else storage.all(City).filter_by(state_id=state.id).all()
        cities_html = ''.join([f'<li>{city.id}: <b>{city.name}</b></li>' for city in cities])
        states_html += f'<li>{state.id}: <b>{state.name}</b><ul>{cities_html}</ul></li>'
    return render_template_string(f'<html><body><h1>States</h1><ul>{states_html}</ul></body></html>')


@app.teardown_appcontext
def close_session(exception=None):
    """Close the storage after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
