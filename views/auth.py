import calendar
import datetime

import jwt as jwt
from flask import request, abort
from flask_restx import Resource, Namespace

from implemented import user_service
from constants import ALGO, SECRET

# Регистрация неймспейса
auth_ns = Namespace('auth')


@auth_ns.route("/")
class AuthView(Resource):
    """CBV"""
    def post(self):
        """Получает логин и пароль из Body запроса в виде JSON, далее проверяет
        соотвествие с данными в БД (есть ли такой пользователь, такой ли у него
        пароль) и если всё оk — генерит пару access_token и refresh_token и от-
        дает их в виде JSON."""
        req_json = request.json
        username = req_json.get("username", None)
        password = req_json.get("password", None)
        if None in [username, password]:
            abort(401)

        user = user_service.get_by_username(username)

        if user is None:
            return {"error": "Неверные учётные данные"}, 401

        data = {
            "username": user.username,
            "password": user.password,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201

    def put(self):
        """получает refresh_token из Body запроса в виде JSON, далее проверяет
        refresh_token и если он не истек и валиден — генерит пару access_token
        и refresh_token и отдает их в виде JSON."""
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if refresh_token is None:
            abort(400)

        try:
            data = jwt.decode(jwt=refresh_token, key=SECRET, algorithms=[ALGO])
        except Exception as e:
            abort(400)

        username = data.get("username")
        password = data.get("password")
        role = data.get("role")

        user = user_service.get_by_username(username)

        data = {
            "username": user.username,
            "password": user.password,
            "role": role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201
