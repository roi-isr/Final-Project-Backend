""" Main app, implementing Restful-API endpoints with Flask frameworks - getting requests from frontend users and
sending back a response """

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from server.resources.admin import AdminRouter
from server.resources.contact import ContactRouter
from server.resources.stock import StockRouter
from server.resources.delivery import DeliveryRouter
from server.resources.store import StoreRouter
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
# Proper exception handling
app.config['PROPAGATE_EXCEPTIONS'] = True

cors = CORS(app)

api = Api(app)
jwt = JWTManager(app)


def add_resources(resources):
    for path, class_name in resources.items():
        api.add_resource(class_name, path)


add_resources(AdminRouter.routes)
add_resources(ContactRouter.routes)
add_resources(StockRouter.routes)
add_resources(DeliveryRouter.routes)
add_resources(StoreRouter.routes)


if __name__ == "__main__":
    app.run(debug=True)
