from flask import Flask
from db import db
from one_to_one import Person, Passport
from one_to_many import Team, Player
from many_to_many import Student, Course
from flask_migrate import Migrate # type: ignore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the single db instance
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "Flask Relationships Example Running"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
