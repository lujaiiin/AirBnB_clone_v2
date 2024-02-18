#!/usr/bin/python3
from flask import Flask, render_template_string, request
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


storage.init_app(app)


@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).order_by(State.name)
    return render_template_string('''
    <html>
        <body>
            <h1>States</h1>
            <ul>
                {% for state in states %}
                    <li>{{ state.id }}: <b>{{ state.name }}</b></li>
                {% endfor %}
            </ul>
        </body>
    </html>
    ''', states=states)


@app.route('/states/<int:state_id>', strict_slashes=False)
def state(state_id):
    state = storage.get(State, state_id)
    if state:
        cities = state.cities.order_by(City.name)
        return render_template_string('''
        <html>
            <body>
                <h1>State: {{ state.name }}</h1>
                <h3>Cities:</h3>
                <ul>
                    {% for city in cities %}
                        <li>{{ city.id }}: <b>{{ city.name }}</b></li>
                    {% endfor %}
                </ul>
            </body>
        </html>
        ''', state=state, cities=cities)
    else:
        return 'Not found!',  404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
