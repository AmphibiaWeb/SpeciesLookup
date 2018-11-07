# everything to do with api creation
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

import os
import time
import kmlparserclass as k
import ray_casting as r
import lookup_table as table

all_species = [name.split('.')[0] for name in next(os.walk('kml'))[1] if name]

grid_cells = table.create_table()


# print(grid_cells)
class User(Resource):
    def get(self, points):
        start = time.clock()
        longa, lat = float(points.split(",")[0]), float(points.split(",")[1])
        i, j = table.grid_cell.array_index(longa, lat, (1, 1))
        point = r.points(longa, lat)
        cell = grid_cells[i][j]
        result = []
        for species in cell.species:
            par = k.parser(species)
            if par.inside(point):
                result.append(species)
        stop = time.clock()
        print(stop - start)
        result.append("count: " + str(len(result)))
        return str(result), 200

    def post(self, points):
        return "method not supported", 404

    def put(self, points):
        return "method not supported", 404

    def delete(self, points):
        return "method not supported", 404


api.add_resource(User, "/api/<string:points>")

if __name__ == '__main__':
    app.run(debug=True)
