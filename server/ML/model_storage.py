import pickle
from server.database.database import Database
from server.database.queries.ML_models import *
from typing import Tuple
import psycopg2


class ModelStorage:
    @staticmethod
    def __get_tuple_pickled(objects_tuple: Tuple):
        return tuple(psycopg2.Binary(pickle.dumps(_obj)) for _obj in objects_tuple)

    @staticmethod
    def __get_tuple_unpickled(bytes_tuple: Tuple):
        return tuple(pickle.loads(_bytes) for _bytes in bytes_tuple)

    @staticmethod
    def __get_unpickled(single_bytes):
        return pickle.loads(single_bytes)

    @staticmethod
    def store_model_in_db(model, scaler_X, scaler_y):
        database = Database()
        database.create_table(CREATE_MODEL_QUERY)
        database.drop_table(DELETE_ALL_MODELS_QUERY)
        pickled_tuple = ModelStorage.__get_tuple_pickled((model, scaler_X, scaler_y))
        database.insert_data(INSERT_MODEL_QUERY, pickled_tuple)
        database.close_connection()

    @staticmethod
    def get_model_from_db():
        database = Database()
        get_data = database.fetch_all_data(GET_MODEL_QUERY)[0]
        print(get_data)
        database.close_connection()
        unpickled_model = ModelStorage.__get_unpickled(get_data[1])
        unpickled_scalers_tuple = ModelStorage.__get_tuple_unpickled((get_data[2], get_data[3]))
        return unpickled_model, unpickled_scalers_tuple
