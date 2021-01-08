""" Main app, implementing Restful-API endpoints with Flask frameworks - getting requests from frontend users and
sending back a response """

from flask import Flask, jsonify, request
from DB import DB
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
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


# Defines the Retrieving of contact-us information API endpoint
class ValidateAuthUser(Resource):
    # Indicates the requirement of an JWT authentication in purpose of reaching the following resources
    @jwt_required()
    def get(self):
        return jsonify({"auth": "Authenticated User"})


api.add_resource(ValidateAuthUser, '/verify-token')


# Defines the Retrieving of contact-us information API endpoint
class ContactUsGet(Resource):
    # Indicates the requirement of an JWT authentication in purpose of reaching the following resources
    @jwt_required()
    def get(self, email):
        database = DB()
        data = database.get_data(email)
        data_dict = {i: data[i] for i in range(len(data))}
        database.close_connection()
        return jsonify(data_dict)


api.add_resource(ContactUsGet, '/contact/<string:email>')


# Defines the Update of contact-us information API endpoint
class ContactUsPost(Resource):
    @staticmethod
    def post():
        database = DB()
        database.create_table()
        data = request.get_json(force=True)
        database.insert_data(list(data.values()))
        database.close_connection()
        return "Successful POST"


api.add_resource(ContactUsPost, '/contact')


# Defines Adding an Admin API endpoint
class AddAdmin(Resource):
    @staticmethod
    def post():
        database = DB()
        database.create_admin_table()
        data = request.get_json(force=True)
        database.add_admin(list(data.values()))
        database.close_connection()
        return "Successful POST"


api.add_resource(AddAdmin, '/add-admin'

# Defines Adding an Admin API endpoint
class DelAdminTable(Resource):
    @staticmethod
    def delete():
        database = DB()
        database.drop_admin_table()
        database.close_connection()
        return "Successful DELETE"


api.add_resource(DelAdminTable, '/drop-admin')

if __name__ == "__main__":
    app.run(debug=True)

