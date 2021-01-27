from typing import List, Tuple
from flask import jsonify
from server.database.database import Database

class ApiHandler:
    def __init__(self):
        self._response = ""

    @staticmethod
    def _build_response(data, status_code):
        response = data
        if not status_code:
            return response
        response.status_code = status_code
        return response

    @staticmethod
    def _create_table(query: str):
        database = Database()
        database.create_table(query)
        database.close_connection()

    def _insert(self, query: str, data: List[str]):
        database = Database()
        tuple_data = tuple(data)
        database.insert_data(query, tuple_data)
        database.close_connection()
        json_info = jsonify({"message": "Successful POST request"})
        self._response = self._build_response(data=json_info, status_code=201)

    def _delete_table(self, query: str):
        database = Database()
        database.drop_table(query)
        database.close_connection()
        json_info = jsonify({"message": "Successful DELETE request"})
        self._response = self._build_response(data=json_info, status_code=200)

    def _fetch_data(self, query: str, data: Tuple[str]):
        database = Database()
        data = database.fetch_specific_data(query, data)
        data_dict = {i: data[i] for i in range(len(data))}
        database.close_connection()
        json_info = jsonify(data_dict)
        self._response = self._build_response(data=json_info, status_code=200)
