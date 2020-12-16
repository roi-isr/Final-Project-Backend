from flask import Flask, jsonify, request
from DB import DB
from flask_restful import Api, Resource
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)


@cross_origin()
class ContactUsGet(Resource):
    def get(self, email):
        database = DB()
        data = database.get_data(email)
        data_dict = {i: data[i] for i in range(len(data))}
        return jsonify(data_dict)


api.add_resource(ContactUsGet, '/contact/<string:email>')


class ContactUsPost(Resource):
    def post(self):
        database = DB()
        data = request.get_json(force=True)
        database.insert_data(list(data.values()))
        return "Successful POST"


api.add_resource(ContactUsPost, '/contact')


# @app.route('/create',)
# def home():
#     database = DB()
#     print(database.get_data('roladin'))
#
#     # conn = connect_to_db()
#     database.create_table()
#     # print("Successful connection and creation")
#     return "successful run"


if __name__=="__main__":
    app.run(port=5000, debug=True)

