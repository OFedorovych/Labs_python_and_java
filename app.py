from flask import Flask, request, jsonify
#from service import ToDoService
#from models import Schema
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'goods.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://alexf:Alex123456788!@localhost/lab_6_db'format(username, password, server)
DATABSE_URI='mysql+mysqlconnector://alexf:Alex123456788!@localhost/lab_6_db'.format(user='alexf', password='Alex123456788!', server='localhost', database='lab_6_db')

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    price = db.Column(db.Float, unique=True)
    weight = db.Column(db.Float, unique=True)
    producer = db.Column(db.String(80), unique=True)
    country = db.Column(db.String(80), unique=True)


    def __init__(self, name, price, weight, producer, country):
        self.name = name
        self.price = price
        self.weight = weight
        self.producer = producer
        self.country = country

    def __repr__(self):
        return '<User %r>' % self.name

class GoodSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'price',  'weight', 'producer', 'country')


good_schema = GoodSchema()
goods_schema = GoodSchema(many=True)
db.create_all()

# endpoint to create new good
@app.route("/good", methods=["POST"])
def add_good():
    name = request.json['name']
    price = request.json['price']
    weight = request.json['weight']
    producer = request.json['producer']
    country = request.json['country']
    
    new_good = Good(name, price, weight, producer, country)

    db.session.add(new_good)
    db.session.commit()

    return jsonify(new_good)

# endpoint to show all goods
@app.route("/all_goods", methods=["GET"])
def get_goods():
    goods = Good.query.all()
    goods_schema = GoodSchema(many=True)
    output = goods_schema.dump(goods)
    return jsonify({'goods': output})

# endpoint to update good
@app.route("/good/<id>", methods=["PUT"])
def good_update(id):
    good = Good.query.get(id)
    name = request.json['name']
    price = request.json['price']
    weight = request.json['weight']
    producer = request.json['producer']
    country = request.json['country']

    good.name = name
    good.price = price
    good.weight = weight
    good.producer = producer
    good.country = country

    db.session.commit()
    return good_schema.jsonify(good)

# endpoint to delete good
@app.route("/good/<id>", methods=["DELETE"])
def good_delete(id):
    good = Good.query.get(id)
    db.session.delete(good)
    db.session.commit()

    return good_schema.jsonify(good)


if __name__ == '__main__':
    app.run(debug=True)
