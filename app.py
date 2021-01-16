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


add_resources(AdminRouter.routes)
add_resources(ContactRouter.routes)


if __name__ == "__main__":
    app.run(debug=True)
