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

    class PackageDelete(Resource):
        @staticmethod
        @jwt_required()
        def delete(code):
            package_handler = StockHandler()
            return package_handler.delete_item(code)

    # Connect between path-->class
    routes = {'/packages': StockGetAll,
              '/package': StockPost,
              '/package/<string:code>': PackageDelete}
