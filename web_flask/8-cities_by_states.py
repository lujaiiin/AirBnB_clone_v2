#!/usr/bin/python3
"""Modules"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ colse"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ci"""
    states = storage.all(State).values()
    for state in states:
        if not hasattr(state, 'cities'):
            setattr(state, 'cities', state.cities)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
