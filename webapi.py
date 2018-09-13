# everything to do with api creation
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self,name):
        return name, 200
    def post(self,name):
        return "method not supported", 404
    def put(self,name):
        return "method not supported", 404
    def delete(self,name):
        return "method not supported", 404

api.add_resource(User,"/user/<string:name>")
app.run(debug=True)
