from dao.model.movie import Movie


class MovieDao:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_movies = self.session.query(Movie).all()
        return all_movies

    def get_one(self, mid: int):
        movie = self.session.query(Movie).get(mid)
        return movie

    def get_by_director_id(self, did: int):
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, gid: int):
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create_movie(self, data):
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def update_movie(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete_movie(self, movie):
        self.session.add(movie)
        self.session.commit()
