from dao.model.genre import Genre


class GenreDAO:
    """ Создание слоя DAO с методами обработки данных """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, genre):
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre
