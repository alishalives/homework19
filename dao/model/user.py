from marshmallow import Schema, fields
from setup_db import db


class User(db.Model):
    """ Создание модели таблицы user """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, nullable=True)
    role = db.Column(db.String, nullable=True)


class UserSchema(Schema):
    """ Создание схемы таблицы user для дальнейшей сериализации """
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
