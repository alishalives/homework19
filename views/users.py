from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

# Регистрация неймспейса
user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    """CBV"""
    def get(self):
        """Метод получения всех пользователей"""
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200

    def post(self):
        """Метод создания пользователя"""
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    """CBV"""
    def get(self, uid):
        """Метод получения пользователя по его id"""
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200

    def put(self, uid):
        """Метод обновления данных о пользователе"""
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid):
        """Метод удаления определенного пользователя"""
        user_service.delete(uid)
        return "", 204


