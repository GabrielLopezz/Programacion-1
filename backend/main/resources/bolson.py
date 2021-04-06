from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'nombre': 'LaGranja', },
    2: {'nombre': 'Timo', },
}

class Bolson(Resource):
    def get(self, id):
        def get(self, id):
            if int(id) in BOLSONES:
                return BOLSONES[int(id)]
            return '', 404


class Bolsones(Resource):
    def get(self):
        return BOLSONES
