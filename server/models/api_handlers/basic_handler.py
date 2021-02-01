from typing import List
from flask import jsonify
from server.database.database import Database
from psycopg2 import errors


class ApiHandler:
    def __init__(self):
        self._response = ""

    @staticmethod
    def _build_response(data, status_code: int):
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
        tuple_data = tuple(data)
        try:
            database = Database()
            database.insert_data(query, tuple_data)
            json_info = jsonify({"message": "Successful POST request"})
            status_code = 201
        except errors.UniqueViolation:
            json_info = jsonify({"message": "Item already exists"})
            status_code = 400
        except:
            json_info = jsonify({"message": "Internal server error"})
            status_code = 500
        finally:
            database.close_connection()
        self._response = self._build_response(data=json_info, status_code=status_code)

    def _fetch_data(self, query: str, data: str, named_values: List[str]):
        try:
            database = Database()
            data = database.fetch_specific_data(query, (data,))
            if data:
                data_dict = {i: {named_values[j]: data[i][j]
                                 for j in range(len(named_values))}
                             for i in range(len(data))}
                json_info = jsonify(data_dict)
                status_code = 200
            else:
                json_info = jsonify({'message': 'Item doesn\'t found'})
                status_code = 404
        except:
            json_info = jsonify({"message": "Internal server error"})
            status_code = 500
        finally:
            database.close_connection()
        print(data_dict)
        self._response = self._build_response(data=json_info, status_code=status_code)

    def _fetch_all_data(self, query: str, named_values: List[str]):
        try:
            database = Database()
            data = database.fetch_all_data(query)
            if data:
                data_dict = {i: {named_values[j]: data[i][j]
                                 for j in range(len(named_values))}
                             for i in range(len(data))}
                json_info = jsonify(data_dict)
                status_code = 200
            else:
                json_info = jsonify({'message': 'Items don\'t found'})
                status_code = 404
        except:
            json_info = jsonify({"message": "Internal server error"})
            status_code = 500
        finally:
            database.close_connection()
        self._response = self._build_response(data=json_info, status_code=status_code)

    def _delete_item(self, query: str, _id: str):
        try:
            database = Database()
            database.delete_item(query, (_id,))
            json_info = jsonify({"message": "Successful DELETE request"})
            status_code = 200
        except:
            json_info = jsonify({"message": "Internal server error"})
            status_code = 500
        finally:
            database.close_connection()
        self._response = self._build_response(data=json_info, status_code=status_code)

    def _drop_table(self, query: str):
        try:
            database = Database()
            database.drop_table(query)
            json_info = jsonify({"message": "Successful DELETE request"})
            status_code = 200
        except:
            json_info = jsonify({"message": "Internal server error"})
            status_code = 500
        finally:
            database.close_connection()
        self._response = self._build_response(data=json_info, status_code=status_code)
