from flask import request, jsonify
from werkzeug.security import safe_str_cmp
from flask_restful import Resource
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                get_jwt_identity)

from server.models.api_handlers.admin import AdminHandler
from ..models.entities.admin import Admin


class AdminRouter:
    class AdminLogIn(Resource):
        @staticmethod
        def post():
            # Get login data (username and password)
            data = request.get_json(force=True)

            # find admin in database
            admin = Admin.find_by_username(data['username'])

            # Check is admin exist in DB and password is valid - AUTHENTICATION PROCESS
            if admin and safe_str_cmp(data['password'], admin.password):
                # Generate access and refresh tokens, given admin ID
                access_token = create_access_token(identity=admin.id, fresh=True)
                refresh_token = create_refresh_token(identity=admin.id)
                response = jsonify({
                    'access_token': access_token,
                    'refresh_token': refresh_token
                })
                response.status_code = 200
                return response

            response = jsonify({'message': 'You have sent invalid credentials'})
            # Send unauthorized message
            response.status_code = 401
            return response

    class TokenRefresher(Resource):
        @staticmethod
        @jwt_required(refresh=True)
        def post():
            # Return the identity of the JWT user that accessing the endpoint
            curr_admin = get_jwt_identity()
            # Generate a new access token
            new_access_token = create_access_token(identity=curr_admin, fresh=False)
            response = jsonify({'access_token': new_access_token})
            response.status_code = 200
            return response

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
    routes = {'/auth': AdminLogIn,
              '/refresh': TokenRefresher,
              '/verify-token': VerifyAuthUser,
              '/add-admin': AddAdmin,
              '/drop-admin': DelAdminTable}
