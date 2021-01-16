from flask_restful import Resource
from server.api_handlers import contact
from flask import request
from flask_jwt import jwt_required


class ContactRouter:
    # Defines the Retrieving of contact-us information API endpoint
    class ContactUsGet(Resource):
        @jwt_required()
        def get(self, email):
            return contact.get_info(email)

    # Defines the Update of contact-us information API endpoint
    class ContactUsPost(Resource):
        @staticmethod
        def post():
            data = request.get_json(force=True)
            return contact.insert(data)

    # Connect between path-->class
    routes = {'/contact/<string:email>': ContactUsGet,
              '/contact': ContactUsPost}
