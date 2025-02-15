""" Main app, implementing Restful-API endpoints with Flask frameworks - getting requests from frontend users and
sending back a response """
import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from server.resources.ML_predictions import PredRouter
from server.resources.admin import AdminRouter
from server.resources.admin_price_advise import AdminAdviseRouter
from server.resources.contact import ContactRouter
from server.resources.delivery import DeliveryRouter
from server.resources.diamond_offer import OfferRouter
from server.resources.sell import SellRouter
from server.resources.stock import StockRouter
from server.resources.store import StoreRouter

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
add_resources(SellRouter.routes)
add_resources(OfferRouter.routes)
add_resources(PredRouter.routes)
add_resources(AdminAdviseRouter.routes)

# build_ml_advise_models()
# build_ml_models()

if __name__ == "__main__":
    app.run(debug=True)

# debug=True
