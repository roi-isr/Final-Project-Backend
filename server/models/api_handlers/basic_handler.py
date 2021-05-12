from typing import List, Tuple
from flask import jsonify
from server.database.database import Database
import psycopg2


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

    def __handle_data(self, data: List[Tuple[str]], named_values: List[str]):
        if data:
            data_dict = {i: {named_values[j]: data[i][j]
                             for j in range(len(named_values))}
                         for i in range(len(data))}
            self._response = self._build_response(data=jsonify(data_dict),
                                                  status_code=200)
        else:
            self._response = self._build_response(data=jsonify({'message': 'Item doesn\'t found'}),
                                                  status_code=404)

    # Fetch specific data (with WHERE)
    def _fetch_data(self, query: str, identifier: str, named_values: List[str]):
        try:
            database = Database()
            data = database.fetch_specific_data(query, (identifier,))
            self.__handle_data(data, named_values)
        except:
            self._response = self._build_response(data=jsonify({"message": "Internal server error"}),
                                                  status_code=500)
        finally:
            database.close_connection()

    def _fetch_all_data(self, query: str, named_values: List[str]):
        try:
            database = Database()
            data = database.fetch_all_data(query)
            self.__handle_data(data, named_values)
        except:
            self._response = self._build_response(data=jsonify({"message": "Internal server error"}),
                                                  status_code=500)
        finally:
            database.close_connection()

    def _insert(self, query: str, data: List[str]):
        tuple_data = tuple(data)
        try:
            database = Database()
            _id = database.insert_data(query, tuple_data)
            self._response = self._build_response(data=jsonify({"message": "Successful POST request", "_id": _id}),
                                                  status_code=201)
        except psycopg2.errors.UniqueViolation:
            self._response = self._build_response(data=jsonify({"message": "Item already exists"}),
                                                  status_code=400)
        except:
            self._response = self._build_response(data=jsonify({"message": "Internal server error"}),
                                                  status_code=500)
        finally:
            database.close_connection()

    def _update_item(self, query: str, _id: str, data: List[str] or str):
        if isinstance(data, list):
            tuple_data = tuple(data)
        else:
            tuple_data = data
        try:
            database = Database()
            print(tuple_data)
            _id = database.update_item(query, tuple_data, _id)
            self._response = self._build_response(data=jsonify({"message": "Successful PUT request", "_id": _id}),
                                                  status_code=200)
        except:
            self._response = self._build_response(data=jsonify({"message": "Internal server error"}),
                                                  status_code=500)
        finally:
            database.close_connection()

    def _delete_item(self, query: str, _id: str):
        try:
            database = Database()
            database.delete_item(query, (_id,))
            self._response = self._build_response(data=jsonify({"message": "Successful DELETE request"}),
                                                  status_code=200)
        except:
            self._response = self._build_response(data=jsonify({"message": "Internal server error"}),
                                                  status_code=500)
        finally:
            database.close_connection()

    def _drop_table(self, query: str):
        try:
            database = Database()
            database.drop_table(query)
            self._response = self._build_response(data=jsonify({"message": "Successful DELETE request"}),
                                                  status_code=200)
        except:
            self._response = self._build_response(data=jsonify({"message": "Internal server error"}),
                                                  status_code=500)
        finally:
            database.close_connection()
