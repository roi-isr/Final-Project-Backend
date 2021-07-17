import hashlib

from flask import request, jsonify
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                get_jwt_identity)
from flask_restful import Resource
from werkzeug.security import safe_str_cmp

from server.models.api_handlers.admin import AdminHandler
from ..models.entities.admin import Admin


# hash the password
def hash_pwd(password: str):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password


class AdminRouter:
    class AdminLogIn(Resource):

        @staticmethod
        def post():
            # Get login data (username and password)
            data = request.get_json(force=True)

            hashed_pwd = hash_pwd(str(data['password']))

            # find admin in database
            admin = Admin.find_by_username(data['username'])

            # Check is admin exist in DB and password is valid - AUTHENTICATION PROCESS
            if admin and safe_str_cmp(hashed_pwd, admin.password):
                # Generate access and refresh tokens, given admin ID
                access_token = create_access_token(identity=admin.id, fresh=True)
                refresh_token = create_refresh_token(identity=admin.id)
                response = jsonify({
                    'access_token': access_token,
                    'refresh_token': refresh_token
                })
                response.status_code = 200
                return response
            if not admin:
                response = jsonify({'message': 'שם משתמש לא קיים במערכת...'})
            else:
                response = jsonify({'message': 'הסיסמא שהוכנסה שגויה'})
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

    # Defines Adding an Admin API endpoint
    class AddAdmin(Resource):
        @staticmethod
        @jwt_required()
        def post():
            admin_handler = AdminHandler()
            data = list(request.get_json(force=True).values())
            return admin_handler.insert(data)

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
              '/add-admin': AddAdmin,
              '/drop-admin': DelAdminTable}
