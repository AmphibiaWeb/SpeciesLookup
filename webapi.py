# everything to do with api creation
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

import os 
import time 
import kmlparserclass as k
import ray_casting as r

all_species = [name.split('.')[0] for name in next(os.walk('kml'))[1] if name]

accoutants = [k.parser(specie) for specie in all_species]

class User(Resource):
    def get(self,points):
        start = time.clock()
        print(points)
        long, lat = float(points.split(",")[0]),float(points.split(",")[1])
        point = r.points(long,lat)
        result = [account.scientific_name for account in accoutants if account.inside(point)]
        stop = time.clock()
        print(stop-start)
        return str(result), 200
        
    def post(self,points):
        return "method not supported", 404
    def put(self,points):
        return "method not supported", 404
    def delete(self,points):
        return "method not supported", 404

api.add_resource(User,"/api/<string:points>")
app.run(debug=True)
