from flask import Flask,jsonify,request
from DB import DB
from flask_restful import Resource,Api
from flask import jsonify

import psycopg2

app = Flask(__name__)
api = Api(app)
class contact_us(Resource):
    # def get(self,keyword):
    #
    #     return jsonify({'keyword'})
    def post(self):
        database=DB()
        data = request.get_json(force=True)
        database.insert_data(list(data.values()))
        return "Successful POST"

api.add_resource(contact_us,'/contact')

@app.route('/create',)
def home():
    database = DB()
    print(database.get_data('roladin'))

    # conn = connect_to_db()
    database.create_table()
    # print("Successful connection and creation")
    return "successful run"

@app.route('/roi')
def roi():
    return "Roi"

@app.route('/daniel')
def daniel():
    return "Daniel"

if __name__=="__main__":
    app.run(port=5000, debug=True)

