from one_to_many import Team, Player
from db import db
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def seed_data():
    with app.app_context():
        db.create_all()

        # Create Team and Player entries
        team1 = Team(name="Manchester United")
        player1 = Player(name="Bruno Fernandes", team=team1)
        player2 = Player(name="Joel Nzuki", team=team1)

        team2 = Team(name="Liverpool")
        player3 = Player(name="Mohammed Salah", team=team2)
        player4 = Player(name="Victor Ndungi", team=team2)

        # Add records to the session and commit
        db.session.add_all([team1, player1, player2, team2, player3, player4])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
