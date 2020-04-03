from flask import Flask, request
from flask_restful import Resource, Api
import getAssingments
app = Flask(__name__)
api = Api(app)

class get_assingments(Resource):
    def get(self):
        body = request.json
        tasks = getAssingments.get(body['username'], body['password'])
        return tasks

class index(Resource):
    def get(self):
        return 'mLibroAPI'

api.add_resource(get_assingments, '/get_assingments')
api.add_resource(index, '/')

if __name__ == "__main__":
    app.run(debug = True)
