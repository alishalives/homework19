from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config: Config = Config()):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    create_data(application, db)


def create_data(app, db):
    """ Функция добавления данных в бд """
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(host="localhost", port=10001, debug=True)
