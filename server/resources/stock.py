from flask_restful import Resource
from server.models.api_handlers.stock import StockHandler
from flask import request
from flask_jwt_extended import jwt_required


class StockRouter:
    # Defines the Retrieving of contact-us information API endpoint
    class StockGetAll(Resource):
        @jwt_required()
        def get(self):
            stock_handler = StockHandler()
            return stock_handler.fetch_all_data()

    # Defines the Update of contact-us information API endpoint
    class StockPost(Resource):
        @staticmethod
        @jwt_required()
        def post():
            stock_handler = StockHandler()
            data = list(request.get_json(force=True).values())
            return stock_handler.insert(data)

    class StockDeleteUpdate(Resource):
        @staticmethod
        @jwt_required()
        def put(_id):
            stock_handler = StockHandler()
            data = list(request.get_json(force=True).values())
            return stock_handler.update_item(_id, data)

        @staticmethod
        @jwt_required()
        def delete(_id):
            stock_handler = StockHandler()
            return stock_handler.delete_item(_id)

    class StockUpdateStatus(Resource):
        @staticmethod
        @jwt_required()
        def put(_id):
            stock_handler = StockHandler()
            # Extract status
            wanted_status = list(request.get_json(force=True).values())[0]
            return stock_handler.update_item_status(_id, wanted_status)

    # Connect between path-->class
    routes = {'/stocks': StockGetAll,
              '/stock': StockPost,
              '/stock/<string:_id>': StockDeleteUpdate,
              '/stock/update-status/<string:_id>': StockUpdateStatus}
