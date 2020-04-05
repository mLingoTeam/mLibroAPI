from flask import Flask, request, make_response, Response
from flask_restful import Resource, Api
import common.services.calendarAddon as calendarAddon


class sync_assingments(Resource):
    def post(self):
        body = request.json
        tasks = body['tasks']
        calendarAddon.sync(tasks)
        return Response(status=200)