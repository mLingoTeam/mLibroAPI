from flask import Flask, request, make_response
from flask_restful import Resource, Api
import common.getAssingments as getAssingments
import json
app = Flask(__name__)
api = Api(app)

class get_assingments(Resource):
    def post(self):
        body = request.json
        tasks = getAssingments.get(body['username'], body['password'])
        return make_response(tasks)

class index(Resource):
    def get(self):
        return 'mLibroAPI'

api.add_resource(get_assingments, '/get_assingments')
api.add_resource(index, '/')

if __name__ == "__main__":
    app.run(debug = True)
