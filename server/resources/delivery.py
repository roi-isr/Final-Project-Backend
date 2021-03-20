from flask_restful import Resource
from server.models.api_handlers.delivery import DeliveryHandler
from flask import request
from flask_jwt_extended import jwt_required


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
        # @cross_origin(headers=['Content-Type', 'Authorization'])
        @jwt_required()
        def post():
            delivery_handler = DeliveryHandler()
            data = request.get_json(force=True).values()
            return delivery_handler.insert(data)

    class DeliveryPut(Resource):
        @staticmethod
        @jwt_required()
        def put(code):
            delivery_handler = DeliveryHandler()
            data = request.get_json(force=True).values()
            return delivery_handler.update_item(code, data)

    class DeliveryDelete(Resource):
        @staticmethod
        @jwt_required()
        def delete(_id):
            delivery_handler = DeliveryHandler()
            return delivery_handler.delete_item(_id)

    # Connect between path-->class
    routes = {'/deliveries': DeliveryGetAll,
              '/delivery': DeliveryPost,
              '/delivery/update/<string:code>': DeliveryPut,
              '/delivery/<string:_id>': DeliveryDelete}


"""
 ---------------DOCS------------------
GET - /deliveries
POST - /delivery
DELETE - /delivery/<string:_id>
"""
