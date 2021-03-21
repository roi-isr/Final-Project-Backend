from flask_restful import Resource
from server.models.api_handlers.contact import ContactHandler
from flask import request
from flask_jwt_extended import jwt_required


class ContactRouter:
    # Defines the Retrieving of contact-us information API endpoint
    class ContactUsGet(Resource):
        @jwt_required()
        def get(self, email):
            contact_handler = ContactHandler()
            return contact_handler.get_info(email)

    class ContactUsGetAll(Resource):
        @jwt_required()
        def get(self):
            contact_handler = ContactHandler()
            return contact_handler.get_info_all()

    # Defines the Update of contact-us information API endpoint
    class ContactUsPost(Resource):
        @staticmethod
        def post():
            contact_handler = ContactHandler()
            data = list(request.get_json(force=True).values())
            return contact_handler.insert(data)

    class ContactUsDelete(Resource):
        @staticmethod
        @jwt_required()
        def delete(_id):
            contact_handler = ContactHandler()
            return contact_handler.delete(_id)

    # Connect between path-->class
    routes = {'/contact/<string:email>': ContactUsGet,
              '/contact/<string:_id>': ContactUsDelete,
              '/contact': ContactUsPost,
              '/contacts': ContactUsGetAll}
