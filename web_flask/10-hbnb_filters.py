#!/usr/bin/python3
from flask import Flask, render_template, request
from ..models import storage
from ..models.state import State
from ..models.city import City
from ..models.amenity import Amenity


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


storage.init_app(app)


@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).order_by(State.name)
    amenities = storage.all(Amenity).order_by(Amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
