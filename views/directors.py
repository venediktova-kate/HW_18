from flask_restx import Namespace, Resource

from implemented import director_service, directors_schema, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        all_directors = director_service.get_all()

        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorViews(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)

        return director_schema.dump(director), 200
