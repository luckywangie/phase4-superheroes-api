from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    db.drop_all()
    db.create_all()

    # ---------------- HEROES ----------------
    ironman = Hero(name="Tony Stark", super_name="Iron Man")
    cap = Hero(name="Steve Rogers", super_name="Captain America")
    thor = Hero(name="Thor Odinson", super_name="Thor")
    hulk = Hero(name="Bruce Banner", super_name="Hulk")
    widow = Hero(name="Natasha Romanoff", super_name="Black Widow")
    hawkeye = Hero(name="Clint Barton", super_name="Hawkeye")
    strange = Hero(name="Stephen Strange", super_name="Doctor Strange")
    spidey = Hero(name="Peter Parker", super_name="Spider-Man")
    tchalla = Hero(name="T'Challa", super_name="Black Panther")
    wanda = Hero(name="Wanda Maximoff", super_name="Scarlet Witch")

    db.session.add_all([ironman, cap, thor, hulk, widow, hawkeye, strange, spidey, tchalla, wanda])

    # ---------------- POWERS ----------------
    flight = Power(name="Flight", description="Allows the user to fly at extreme speeds through the air.")
    super_strength = Power(name="Super Strength", description="Grants enhanced physical strength far beyond human limits.")
    shield_mastery = Power(name="Shield Mastery", description="Expert usage of a vibranium shield with acrobatic skills.")
    thunder = Power(name="Thunder Control", description="Can summon and control lightning and storms.")
    rage = Power(name="Rage Mode", description="Transforms the user into a rage-powered form with massive strength.")
    stealth = Power(name="Stealth", description="Advanced espionage and stealth combat techniques.")
    precision = Power(name="Precision Archery", description="Mastery of bows with near-perfect accuracy.")
    magic = Power(name="Mystic Arts", description="Command over magical energy, portals, and time-based spells.")
    agility = Power(name="Wall-Crawling Agility", description="Grants wall-crawling and enhanced reflexes and agility.")
    telekinesis = Power(name="Chaos Magic", description="Can move and manipulate objects using mental energy.")

    db.session.add_all([flight, super_strength, shield_mastery, thunder, rage, stealth, precision, magic, agility, telekinesis])

    # ---------------- HERO POWERS ----------------
    db.session.add_all([
        HeroPower(hero=ironman, power=flight, strength="Strong"),
        HeroPower(hero=ironman, power=super_strength, strength="Average"),

        HeroPower(hero=cap, power=shield_mastery, strength="Strong"),
        HeroPower(hero=cap, power=super_strength, strength="Strong"),

        HeroPower(hero=thor, power=thunder, strength="Strong"),
        HeroPower(hero=thor, power=flight, strength="Average"),

        HeroPower(hero=hulk, power=rage, strength="Strong"),
        HeroPower(hero=hulk, power=super_strength, strength="Strong"),

        HeroPower(hero=widow, power=stealth, strength="Strong"),

        HeroPower(hero=hawkeye, power=precision, strength="Strong"),

        HeroPower(hero=strange, power=magic, strength="Strong"),

        HeroPower(hero=spidey, power=agility, strength="Strong"),

        HeroPower(hero=tchalla, power=stealth, strength="Average"),
        HeroPower(hero=tchalla, power=super_strength, strength="Average"),

        HeroPower(hero=wanda, power=telekinesis, strength="Strong"),
        HeroPower(hero=wanda, power=magic, strength="Strong"),
    ])

    db.session.commit()

print(" Database seeded with Avengers and powers!")
