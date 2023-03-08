from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from helpers.decorators import auth_required, admin_required
from implemented import director_service

# Регистрация неймспейса
director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    """CBV"""
    @auth_required
    def get(self):
        """Получение данных обо всех режиссерах при наличии токена"""
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        """Добавление нового режиссера при наличии прав admin"""
        req_json = request.json
        director = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """CBV"""
    @auth_required
    def get(self, did):
        """Получение данных о режиссере при наличии токена"""
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, did):
        """Обновление данных о режиссере при наличии прав admin"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, did):
        """Удаление данных о режиссере при наличии прав admin"""
        director_service.delete(did)
        return "", 204
