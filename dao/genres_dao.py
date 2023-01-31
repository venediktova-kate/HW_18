from dao.model.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_genres = self.session.query(Genre).all()
        return all_genres

    def get_one(self, did: int):
        genre = self.session.query(Genre).get(did)
        return genre
