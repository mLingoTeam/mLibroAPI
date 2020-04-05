from flask import Flask, request, make_response, Response
from flask_restful import Resource, Api
import common.getAssingments as getAssingments
import json
import common.services.calendarAddon as calendarAddon
app = Flask(__name__)
api = Api(app)

class get_assingments(Resource):
    def post(self):
        body = request.json
        tasks = getAssingments.get(body['username'], body['password'])
        if tasks is None:
            return Response(status=403)
        return make_response(tasks)

class refresh_assingments(Resource):
    def post(self):
        body = request.json
        token = body['token']
        tasks = getAssingments.refresh(token)
        if tasks is None:
            return Response(status=403)
        return make_response(tasks)


class sync_assingments(Resource):
    def post(self):
        body = request.json
        tasks = body['tasks']
        calendarAddon.sync(tasks)
        return Response(status=200)


class index(Resource):
    def get(self):
        return 'mLibroAPI'

api.add_resource(get_assingments, '/get_assingments')
api.add_resource(sync_assingments, '/calendar_sync')
api.add_resource(refresh_assingments, '/refresh')
api.add_resource(index, '/')

if __name__ == "__main__":
    app.run(debug = True)
