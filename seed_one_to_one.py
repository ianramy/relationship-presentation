from one_to_one import Person, Passport
from db import db
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def seed_data():
    with app.app_context():
        db.create_all()

        # Create Person and Passport entries
        person1 = Person(name="Peninah John")
        passport1 = Passport(passport_number="A1234567", person=person1)

        person2 = Person(name="Savio Sentamu")
        passport2 = Passport(passport_number="B7654321", person=person2)

        db.session.add_all([person1, passport1, person2, passport2])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
