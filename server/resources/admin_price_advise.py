from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from server.models.api_handlers.admin_price_advise import AdminAdviseHandler


class AdminAdviseRouter:
    # Defines the Retrieving of admin advise information API endpoint
    class AdminAdviseGetAll(Resource):
        @jwt_required()
        def get(self):
            admin_advise_handler = AdminAdviseHandler()
            return admin_advise_handler.fetch_all_data()

    # Defines the Update of contact-us information API endpoint
    class AdminAdvisePost(Resource):
        @staticmethod
        # @cross_origin(headers=['Content-Type', 'Authorization'])
        @jwt_required()
        def post():
            admin_advise_handler = AdminAdviseHandler()
            data = list(request.get_json(force=True).values())
            return admin_advise_handler.insert(data)

    # Connect between path-->class
    routes = {'/admin-advises': AdminAdviseGetAll,
              '/admin-advise': AdminAdvisePost}
