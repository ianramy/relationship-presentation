from db import db

# Example: Person and Passport (One-to-One relationship)
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # One-to-One relationship with Passport
    passport = db.relationship('Passport', backref='person', uselist=False)

class Passport(db.Model):
    __tablename__ = 'passport'
    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(20), unique=True, nullable=False)

    # Foreign key to link Passport to Person
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
