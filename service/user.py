import hashlib

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        user = self.get_one(data.get("id"))
        user.username = data.get("username")
        user.password = self.get_hash(data.get("password"))
        user.role = data.get("role")
        self.dao.update(user)

    def delete(self, uid):
        user = self.get_one(uid)
        self.dao.delete(user)

