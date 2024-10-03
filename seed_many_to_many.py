from many_to_many import Student, Course
from db import db
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def seed_data():
    with app.app_context():
        db.create_all()

        # Create Student and Course entries
        student1 = Student(name="Dorcus")
        student2 = Student(name="Ian")

        course1 = Course(name="Phase 4")
        course2 = Course(name="Phase 5")

        # Associate students with courses (many-to-many)
        student1.courses = [course1, course2]
        student2.courses = [course2, course1]

        # Add records to the session and commit
        db.session.add_all([student1, student2, course1, course2])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
