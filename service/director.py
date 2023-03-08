from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        director = self.get_one(data.get("id"))
        director.name = data.get("name")
        self.dao.update(director)

    def delete(self, did):
        director = self.get_one(did)
        self.dao.delete(director)
