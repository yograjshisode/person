# This module has code for generating response. This is to keep the response consistent.
from flask import jsonify,  make_response
from flask_api import status


class ResponseGenerator:
    def __init__(self, message='', status_code=None, errors=None, data=None, type=None):
        self.message = message
        self.status = status_code
        self.errors = errors if errors else {}
        self.type = type if type else ""
        self.data = data if data else []

    def make_success_response(self):
        resp_data = self.data
        resp = make_response(jsonify(resp_data), self.status or status.HTTP_200_OK)
        resp.mimetype = 'application/json'
        return resp

    def make_error_response(self):
        resp_data = dict()
        resp_data['message'] = self.message
        resp_data["errors"] = self.errors
        resp_data["type"] = self.type
        resp_data["success"] = False
        resp = make_response(jsonify(resp_data), self.status or status.HTTP_400_BAD_REQUEST)
        resp.mimetype = 'application/json'
        return resp
