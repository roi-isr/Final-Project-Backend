from flask_restful import Resource
from server.models.api_handlers.delivery import DeliveryHandler
from flask import request
from flask_cors import cross_origin
from flask_jwt import jwt_required


class DeliveryRouter:
    # Defines the Retrieving of contact-us information API endpoint
    class DeliveryGetAll(Resource):
        @jwt_required()
        def get(self):
            delivery_handler = DeliveryHandler()
            return delivery_handler.fetch_all_data()

    # Defines the Update of contact-us information API endpoint
    class DeliveryPost(Resource):
        @staticmethod
        @jwt_required()
        def post():
            delivery_handler = DeliveryHandler()
            data = request.get_json(force=True).values()
            return delivery_handler.insert(data)

    class DeliveryDelete(Resource):
        @staticmethod
        @jwt_required()
        def delete(_id):
            delivery_handler = DeliveryHandler()
            return delivery_handler.delete_item(_id)

    # Connect between path-->class
    routes = {'/deliveries': DeliveryGetAll,
              '/delivery': DeliveryPost,
              '/delivery/<string:_id>': DeliveryDelete}


"""
 ---------------DOCS------------------
GET - /deliveries
POST - /delivery
DELETE - /delivery/<string:_id>

"""
