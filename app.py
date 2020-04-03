from flask import Flask, request
from flask_restful import Resource, Api
import getAssingments
app = Flask(__name__)
api = Api(app)

class mLibroApi(Resource):
    def get(self):
        body = request.json
        tasks = getAssingments.get(body['username'], body['password'])
        return tasks
        

api.add_resource(mLibroApi, '/get_assingments')

if __name__ == "__main__":
    app.run(debug = True)
