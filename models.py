from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    role_id = db.Column(db.String(80), db.ForeignKey("role.role"))
    morada= db.Column(db.String(80), nullable=False)
    


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)
    user = db.relationship("User", backref="role")