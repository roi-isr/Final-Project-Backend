from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from server.models.api_handlers.diamond_offer import OfferHandler


class OfferRouter:
    # Defines the Retrieving of sells API endpoint
    class OfferGetAll(Resource):
        @jwt_required()
        def get(self):
            offer_handler = OfferHandler()
            return offer_handler.fetch_all_data()

    # Defines the Update of contact-us information API endpoint
    class OfferPost(Resource):
        @staticmethod
        def post(package_id):
            offer_handler = OfferHandler()
            data = list(request.get_json(force=True).values())
            return offer_handler.insert(data, package_id)

    class OfferDeleteUpdate(Resource):
        @staticmethod
        @jwt_required()
        def delete(_id):
            offer_handler = OfferHandler()
            return offer_handler.delete_item(_id)

    # Connect between path-->class
    routes = {'/offers': OfferGetAll,
              '/offer/<string:package_id>': OfferPost,
              '/offer/<string:_id>': OfferDeleteUpdate}
