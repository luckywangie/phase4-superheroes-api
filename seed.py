from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add Heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    db.session.add_all([hero1, hero2])

    # Add Powers
    power1 = Power(name="super strength", description="gives the wielder super-human strengths")
    power2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    db.session.add_all([power1, power2])

    # Add HeroPowers
    hp1 = HeroPower(strength="Strong", hero=hero1, power=power2)
    db.session.add(hp1)

    db.session.commit()
print("Database seeded with initial data")  # Print a success message