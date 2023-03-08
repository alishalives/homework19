from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from helpers.decorators import auth_required, admin_required
from implemented import genre_service

# Регистрация неймспейса
genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    """CBV"""
    @auth_required
    def get(self):
        """Получение всех жанров, но только при наличии токена"""
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """Добавление жанров при наличии у пользователя прав admin"""
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """CBV"""
    @auth_required
    def get(self, gid):
        """Получение данных об определенном жанре при наличии токена"""
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, gid):
        """Обновление данных о жанре при наличии прав admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, gid):
        """Удаление данных о жанре при наличии прав admin"""
        genre_service.delete(gid)
        return "", 204
