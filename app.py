from flask import Flask, jsonify, request
from DB import DB
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class ContactUsGet(Resource):
    def get(self, email):
        database = DB()
        data = database.get_data(email)
        data_dict = {i: data[i] for i in range(len(data))}
        database.close_connection()
        return jsonify(data_dict)


api.add_resource(ContactUsGet, '/contact/<string:email>')


class ContactUsPost(Resource):
    def post(self):
        database = DB()
        data = request.get_json(force=True)
        database.insert_data(list(data.values()))
        database.close_connection()
        return "Successful POST"


api.add_resource(ContactUsPost, '/contact')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
