from dao.model.director import Director


class DirectorDAO:
    """ Создание слоя DAO с методами обработки данных """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, director):
        self.session.delete(director)
        self.session.commit()

    def update(self, director):
        self.session.add(director)
        self.session.commit()
        return director
