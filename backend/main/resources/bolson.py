from flask_restful import Resource
from flask import request

BOLSONES = {
    1: {'primer bolson': 'Bolson1'},
    2: {'segundo bolson': 'Bolson2'},
    3: {'tercer bolson': 'Bolson3'},
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
