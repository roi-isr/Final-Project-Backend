from flask_restful import Resource
from server.models.api_handlers.diamond_package import PackageHandler
from flask import request
from flask_jwt import jwt_required


class PackageRouter:
    # Defines the Retrieving of contact-us information API endpoint
    class PackageGetAll(Resource):
        @jwt_required()
        def get(self):
            package_handler = PackageHandler()
            return package_handler.fetch_all_data()

    # Defines the Update of contact-us information API endpoint
    class PackagePost(Resource):
        @staticmethod
        @jwt_required()
        def post():
            package_handler = PackageHandler()
            data = request.get_json(force=True).values()
            return package_handler.insert(data)

    class PackageDelete(Resource):
        @staticmethod
        @jwt_required()
        def delete(code):
            package_handler = PackageHandler()
            return package_handler.delete_item(code)

    # Connect between path-->class
    routes = {'/packages': PackageGetAll,
              '/package': PackagePost,
              '/package/<string:code>': PackageDelete}
