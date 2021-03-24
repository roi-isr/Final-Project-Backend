from flask_restful import Resource
from server.models.api_handlers.sell import SellHandler
from flask import request
from flask_jwt_extended import jwt_required


class SellRouter:
    # Defines the Retrieving of sells API endpoint
    class SellGetAll(Resource):
        @jwt_required()
        def get(self):
            sell_handler = SellHandler()
            return sell_handler.fetch_all_data()

    # Defines the Update of contact-us information API endpoint
    class SellPost(Resource):
        @staticmethod
        @jwt_required()
        def post():
            sell_handler = SellHandler()
            data = list(request.get_json(force=True).values())
            return sell_handler.insert(data)

    class SellDeleteUpdate(Resource):
        @staticmethod
        @jwt_required()
        def put(_id):
            sell_handler = SellHandler()
            data = list(request.get_json(force=True).values())
            return sell_handler.update_item(_id, data)

        @staticmethod
        @jwt_required()
        def delete(_id):
            sell_handler = SellHandler()
            return sell_handler.delete_item(_id)

    # Connect between path-->class
    routes = {'/sells': SellGetAll,
              '/sell': SellPost,
              '/sell/<string:_id>': SellDeleteUpdate}
