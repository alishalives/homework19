from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    """ Создание модели таблицы genre """
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    """ Создание схемы таблицы genre для дальнейшей сериализации """
    id = fields.Int()
    name = fields.Str()
