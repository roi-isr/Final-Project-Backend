from flask_restful import Resource
from server.api_handlers.admin import AdminHandler
from flask import request
from flask_jwt import jwt_required


class AdminRouter:
    class VerifyAuthUser(Resource):
        # Indicates the requirement of an JWT authentication in purpose of reaching the following resources
        @staticmethod
        @jwt_required()
        def get():
            admin_handler = AdminHandler()
            return admin_handler.verified()

    # Defines Adding an Admin API endpoint
    class AddAdmin(Resource):
        @staticmethod
        @jwt_required()
        def post():
            admin_handler = AdminHandler()
            data = request.get_json(force=True).values()
            return admin_handler.insert(data)

    # class DelAdmin(Resource):
    #     @staticmethod
    #     @jwt_required()
    #     def delete():
    #         data = request.get_json(force=True)
    #         return admin.delete()

    # Defines Adding an Admin API endpoint
    class DelAdminTable(Resource):
        @staticmethod
        @jwt_required()
        def delete():
            admin_handler = AdminHandler()
            return admin_handler.delete_table()

    # Connect between path-->class
    routes = {'/verify-token': VerifyAuthUser,
              '/add-admin': AddAdmin,
              '/drop-admin': DelAdminTable}
