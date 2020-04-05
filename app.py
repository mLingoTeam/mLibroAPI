from flask import Flask, request, make_response, Response
from flask_restful import Resource, Api
from common.api.get_assingments import get_assingments
from common.api.refresh_assingments import refresh_assingments

app = Flask(__name__)
api = Api(app)


class index(Resource):
    def get(self):
        return 'mLibroAPI'

api.add_resource(get_assingments, '/get_assingments')
api.add_resource(refresh_assingments, '/refresh')
api.add_resource(index, '/')

if __name__ == "__main__":
    app.run(debug = True)
