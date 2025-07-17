from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    EventName = db.Column(db.String(100), nullable=False)
    Date = db.Column(db.String(20), nullable=False)
    Location = db.Column(db.String(100), nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    rsvps = db.relationship('RSVP', backref='event',cascade="all, delete-orphan", lazy=True)

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
