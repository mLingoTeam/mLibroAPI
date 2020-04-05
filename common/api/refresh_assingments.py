from flask import Flask, request, make_response, Response
from flask_restful import Resource, Api
import common.services.librus_api.getAssingments as getAssingments

class refresh_assingments(Resource):
    def post(self):
        body = request.json
        token = body['token']
        tasks = getAssingments.refresh(token)
        if tasks is None:
            return Response(status=403)
        return make_response(tasks)