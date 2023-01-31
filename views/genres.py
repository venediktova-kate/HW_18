from flask_restx import Namespace, Resource

from implemented import genre_service, genres_schema, genre_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        all_genres = genre_service.get_all()

        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreViews(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)

        return genre_schema.dump(genre), 200
