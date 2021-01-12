""" Main app, implementing Restful-API endpoints with Flask frameworks - getting requests from frontend users and
sending back a response """

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from server.api_end_points import admin, contact
from server.security import authenticate, identity
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
# Proper exception handling
app.config['PROPAGATE_EXCEPTIONS'] = True
cors = CORS(app)
api = Api(app)
# create an endpoint path '/auth'
jwt = JWT(app, authenticate, identity)


def add_resources(resources):
    for path, class_name in resources.items():
        api.add_resource(class_name, path)


class AdminApi:
    class VerifyAuthUser(Resource):
        # Indicates the requirement of an JWT authentication in purpose of reaching the following resources
        @jwt_required()
        def get(self):
            return admin.verified()

    # Defines Adding an Admin API endpoint
    class AddAdmin(Resource):
        @staticmethod
        def post():
            data = request.get_json(force=True)
            return admin.add(data)

    # Defines Adding an Admin API endpoint
    class DelAdminTable(Resource):
        @staticmethod
        def delete():
            return admin.delete_table()


resources = {'/add-admin': AdminApi.AddAdmin,
             '/verify-token': AdminApi.VerifyAuthUser,
             '/drop-admin': AdminApi.DelAdminTable}
add_resources(resources)


class ContactApi:
    # Defines the Retrieving of contact-us information API endpoint
    class ContactUsGet(Resource):
        @jwt_required()
        def get(self, email):
            return contact.get_info(email)

    # Defines the Update of contact-us information API endpoint
    class ContactUsPost(Resource):
        @staticmethod
        def post():
            data = request.get_json(force=True)
            return contact.insert(data)


resources = {'/contact': ContactApi.ContactUsPost,
             '/contact/<string:email>': ContactApi.ContactUsGet}
add_resources(resources)


if __name__ == "__main__":
    app.run(debug=True)

