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
            data = request.get_json(force=True).values()
            return stock_handler.insert(data)

    class StockPut(Resource):
        @staticmethod
        @jwt_required()
        def put(code):
            stock_handler = StockHandler()
            data = request.get_json(force=True).values()
            return stock_handler.update_item(code, data)

    class StockDelete(Resource):
        @staticmethod
        @jwt_required()
        def delete(code):
            stock_handler = StockHandler()
            return stock_handler.delete_item(code)

    # Connect between path-->class
    routes = {'/stocks': StockGetAll,
              '/stock': StockPost,
              '/stock/update/<string:code>': StockPut,
              '/stock/<string:code>': StockDelete}
