from flask_restful import Resource, request
from server.resources.sell import SellHandler
from flask import jsonify
from flask_jwt_extended import jwt_required
from server.ML.ML_main import exec_predictions


class PredRouter:
    # Defines the Retrieving of sells API endpoint
    class PredGet(Resource):
        @jwt_required()
        def get(self):
            weight = request.args.get('weight')
            cut = request.args.get('cut')
            color = request.args.get('color')
            clarity = request.args.get('clarity')
            depth = request.args.get('depth')
            table = request.args.get('table')
            data_list = [weight, cut, color, clarity, depth, table]
            if None in data_list:
                response = jsonify({'message': 'Invalid request query params'})
                response.status_code = 400
                return response
            price_prediction = exec_predictions(data_list)
            return jsonify({'price-prediction': price_prediction})

    class InsertSellData(Resource):
        @staticmethod
        @jwt_required()
        def post():
            sell_handler = SellHandler()
            data = list(request.get_json(force=True).values())
            return sell_handler.insert_sell_ml(data)

    # Connect between path-->class
    routes = {'/predict-price': PredGet,
              '/sell-data': InsertSellData}
