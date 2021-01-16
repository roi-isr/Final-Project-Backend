from flask_restful import Resource
from server.api_handlers.contact import ContactHandler
from flask import request
from flask_jwt import jwt_required


class ContactRouter:
    # Defines the Retrieving of contact-us information API endpoint
    class ContactUsGet(Resource):
        @jwt_required()
        def get(self, email):
            contact_handler = ContactHandler()
            return contact_handler.get_info(email)

    # Defines the Update of contact-us information API endpoint
    class ContactUsPost(Resource):
        @staticmethod
        def post():
            contact_handler = ContactHandler()
            data = request.get_json(force=True)
            return contact_handler.insert(data)

    # Connect between path-->class
    routes = {'/contact/<string:email>': ContactUsGet,
              '/contact': ContactUsPost}
