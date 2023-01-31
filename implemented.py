from dao.directors_dao import DirectorDao
from dao.genres_dao import GenreDao
from dao.movies_dao import MovieDao

from dao.model.genre import GenreSchema
from dao.model.movie import MovieSchema
from dao.model.director import DirectorSchema


from service.directors_service import DirectorService
from service.genres_service import GenreService
from service.movies_service import MovieService

from setup_db import db

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
