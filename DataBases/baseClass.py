from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    right_tables = db.relationship('RightTable', backref='user', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    nr_of_database = db.Column(db.Integer, unique=True, nullable=False)

    # Relacja do `RightTable` (jeśli potrzebujesz odwołań)
    right_tables = db.relationship('RightTable', backref='game', lazy=True)
    def __repr__(self):
        return f"Game('{self.name}', '{self.nr_of_database}')"

class RightTable(db.Model):
    __tablename__ = 'rightTable'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    gameId = db.Column(db.Integer,db.ForeignKey('game.id'), nullable=False)
    user = db.relationship('User', backref='rightTable', lazy=True)
    game = db.relationship('Game', backref='rightTable', lazy=True)

    def __repr__(self):
        return f"RightTable('{self.user}', '{self.game}')"
