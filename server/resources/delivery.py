from flask_restful import Resource
from server.models.api_handlers.delivery import DeliveryHandler
from flask import request
from flask_jwt_extended import jwt_required


class DeliveryRouter:
    # Defines the Retrieving of delivery information API endpoint
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
            data = list(request.get_json(force=True).values())
            return delivery_handler.insert(data)

    class DeliveryDeleteUpdate(Resource):
        @staticmethod
        @jwt_required()
        def put(_id):
            delivery_handler = DeliveryHandler()
            data = list(request.get_json(force=True).values())
            return delivery_handler.update_item(_id, data)

        @staticmethod
        @jwt_required()
        def delete(_id):
            delivery_handler = DeliveryHandler()
            return delivery_handler.delete_item(_id)

    class DeliveryMoveToStock(Resource):
        @staticmethod
        @jwt_required()
        def put(_id):
            delivery_handler = DeliveryHandler()
            return delivery_handler.move_to_stock(_id)

    # Connect between path-->class
    routes = {'/deliveries': DeliveryGetAll,
              '/delivery': DeliveryPost,
              '/delivery/<string:_id>': DeliveryDeleteUpdate,
              '/delivery/move-to-stock/<string:_id>': DeliveryMoveToStock}


"""
 ---------------DOCS------------------
GET - /deliveries
POST - /delivery
DELETE - /delivery/<string:_id>
"""
