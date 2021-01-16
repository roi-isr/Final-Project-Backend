from .build_response.build_response import build_response
from flask import jsonify
from server.database.database import Database

class ApiHandler:
    def __init__(self):
        self._response = ""

    @staticmethod
    def _create_table(query):
        database = Database()
        database.create_table(query)
        database.close_connection()

    def _insert(self, query, data):
        database = Database()
        tuple_data = tuple(data)
        database.insert_data(query, tuple_data)
        database.close_connection()
        json_info = jsonify({"message": "Successful POST request"})
        self._response = build_response(data=json_info, status_code=201)

    def _delete_table(self, query):
        database = Database()
        database.drop_table(query)
        database.close_connection()
        json_info = jsonify({"message": "Successful DELETE request"})
        self._response = build_response(data=json_info, status_code=200)

    def _fetch_data(self, query, data):
        database = Database()
        data = database.fetch_specific_data(query, data)
        data_dict = {i: data[i] for i in range(len(data))}
        database.close_connection()
        json_info = jsonify(data_dict)
        self._response = build_response(data=json_info, status_code=200)
