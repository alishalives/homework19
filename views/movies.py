from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from helpers.decorators import auth_required, admin_required
from implemented import movie_service

# Регистрация неймспейса
movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    """CBV"""
    @auth_required
    def get(self):
        """Получение данных о фильмах, но только при наличии токена"""
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200

    @admin_required
    def post(self):
        """Создание новой записи о фильме, но только для пользователей с правами admin"""
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    """CBV"""
    @auth_required
    def get(self, bid):
        """Получение определенного фильма, но только при наличии токена"""
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, bid):
        """Обновление данных о фильме, но только для пользователей с правами admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, bid):
        """Удаление данных о фильме, но только для пользователей с правами admin"""
        movie_service.delete(bid)
        return "", 204
