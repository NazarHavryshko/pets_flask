from flask_login import UserMixin

from . import db


class Users(db.Model, UserMixin):
    __tabelname__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, nullable=False)
    birthday = db.Column(db.Date)
    password = db.Column(db.String(256), nullable=False)
    phoneNumber = db.Column(db.String(13))
    city = db.Column(db.String(40))
