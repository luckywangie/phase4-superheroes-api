#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return {'message': 'Superheroes API'}

#  HERO ROUTES 

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = []
    for hero in heroes:
        result.append(hero.to_dict(nested=True))
    return jsonify(result), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict(nested=True)), 200

# POWER ROUTES

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    result = []
    for power in powers:
        result.append(power.to_dict())
    return jsonify(result), 200

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    try:
        power.from_dict(data, skip_unknown=True)
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

#  HERO POWER ROUTES 

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        hp = HeroPower()
        hp.from_dict(data)
        db.session.add(hp)
        db.session.commit()
        return jsonify(hp.to_dict(nested=True)), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

# MAIN 

if __name__ == '__main__':
    app.run(port=5000, debug=True)
