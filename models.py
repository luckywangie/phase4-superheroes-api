from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerialize
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

# Setup
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
fs_mixin = FlaskSerialize(db)

# Hero 
class Hero(db.Model, fs_mixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(50), nullable=False)

    hero_powers = db.relationship("HeroPower", backref="hero", lazy=True, cascade="all, delete-orphan")

# Power 
class Power(db.Model, fs_mixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    hero_powers = db.relationship("HeroPower", backref="power", lazy=True, cascade="all, delete-orphan")

    @validates("description")
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters.")
        return value

#  HeroPower 
class HeroPower(db.Model, fs_mixin):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    @validates("strength")
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'.")
        return value
