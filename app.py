""" Main app, implementing Restful-API endpoints with Flask frameworks """

from flask import Flask, jsonify, request
from DB import DB
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'ALEX'
api = Api(app)
# create an endpoint path '/auth'
jwt = JWT(app, authenticate, identity)


# Implements the retrieving of contact information endpoint
class ContactUsGet(Resource):
    # Requires an JWT authentication for reach those resources
    @jwt_required()
    def get(self, email):
        database = DB()
        data = database.get_data(email)
        data_dict = {i: data[i] for i in range(len(data))}
        database.close_connection()
        return jsonify(data_dict)


api.add_resource(ContactUsGet, '/contact/<string:email>')


# Implement updating contact information endpoint
class ContactUsPost(Resource):
    def post(self):
        database = DB()
        database.create_table()
        data = request.get_json(force=True)
        database.insert_data(list(data.values()))
        database.close_connection()
        return "Successful POST"


api.add_resource(ContactUsPost, '/contact')


# Implement add admin endpoint
class AddAdmin(Resource):
    def post(self):
        database = DB()
        database.create_admin_table()
        data = request.get_json(force=True)
        database.add_admin(list(data.values()))
        database.close_connection()
        return "Successful POST"


api.add_resource(AddAdmin, '/add-admin')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
