from dao.model.user import User


class UserDAO:
    """ Создание слоя DAO с методами обработки данных """
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, user):
        self.session.delete(user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
