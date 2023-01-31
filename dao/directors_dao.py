from dao.model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_directors = self.session.query(Director).all()
        return all_directors

    def get_one(self, did: int):
        director = self.session.query(Director).get(did)
        return director
