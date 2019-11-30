from flask import Flask, request
from flask_restful import Api

from resources.item import Item, ItemList

app = Flask(__name__)
app = Flask(__name__)

#todo: configure with mariadb
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Item, '/items/<string:id>')
api.add_resource(ItemList, '/items')

if (__name__ == '__main__'):
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

# starting virtual env:
# source venv/bin/activate
# starting server:
# python app.py