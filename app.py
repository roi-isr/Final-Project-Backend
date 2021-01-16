""" Main app, implementing Restful-API endpoints with Flask frameworks - getting requests from frontend users and
sending back a response """

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from server.routers.admin import AdminRouter
from server.routers.contact import ContactRouter
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


api.add_resource(AddAdmin, '/add-admin')

# Defines Adding an Admin API endpoint
class DelAdminTable(Resource):
    @staticmethod
    def delete():
        database = DB()
        database.drop_admin_table()
        database.close_connection()
        return "Successful DELETE"


api.add_resource(DelAdminTable, '/drop-admin')

add_resources(AdminRouter.routes)
add_resources(ContactRouter.routes)


if __name__ == "__main__":
    app.run(debug=True)
