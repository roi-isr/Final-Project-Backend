from flask_restful import Resource
from server.models.api_handlers.store import StoreHandler
from flask_jwt_extended import jwt_required


class StoreRouter:
    # Defines the Retrieving of store information API endpoint
    class StoreGetAll(Resource):
        @staticmethod
        def get():
            store_handler = StoreHandler()
            return store_handler.fetch_all_data()

    # Connect between path-->class
    routes = {'/store-items': StoreGetAll}
