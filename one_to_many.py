from db import db

# Example: Team and Player (One-to-Many relationship)
class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # One team can have many players
    players = db.relationship('Player', backref='team', lazy=True)

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # Foreign key to link Player to Team
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
