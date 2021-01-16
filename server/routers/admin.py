from flask_restful import Resource
from server.api_handlers import admin
from flask import request
from flask_jwt import jwt_required


class AdminRouter:
    class VerifyAuthUser(Resource):
        # Indicates the requirement of an JWT authentication in purpose of reaching the following resources
        @staticmethod
        @jwt_required()
        def get():
            return admin.verified()

    # Defines Adding an Admin API endpoint
    class AddAdmin(Resource):
        @staticmethod
        @jwt_required()
        def post():
            data = request.get_json(force=True)
            return admin.add(data)

    class DelAdmin(Resource):
        @staticmethod
        @jwt_required()
        def delete():
            data = request.get_json(force=True)
            return admin.delete()

    # Defines Adding an Admin API endpoint
    class DelAdminTable(Resource):
        @staticmethod
        @jwt_required()
        def delete():
            return admin.delete_table()

    # Connect between path-->class
    routes = {'/verify-token': VerifyAuthUser,
              '/add-admin': AddAdmin,
              '/drop-admin': DelAdminTable}
