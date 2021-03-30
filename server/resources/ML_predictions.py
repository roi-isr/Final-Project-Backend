from flask_restful import Resource, request
from flask import jsonify
from flask_jwt_extended import jwt_required
from server.ML.test import exec_predictions


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
    # Connect between path-->class
    routes = {'/predict-price': PredGet}
