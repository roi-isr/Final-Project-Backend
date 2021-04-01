import pickle
from server.database.database import Database
from server.database.queries.ML_models import *
from server.database.queries.ML_admin_advise import *
from server.database.queries.admin_price_advice import *
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
    def store_main_model_in_db(model, scaler_X, scaler_y):
        database = Database()
        database.create_table(CREATE_MODEL_QUERY)
        database.drop_table(DELETE_ALL_MODELS_QUERY)
        pickled_tuple = ModelStorage.__get_tuple_pickled((model, scaler_X, scaler_y))
        database.insert_data(INSERT_MODEL_QUERY, pickled_tuple)
        database.close_connection()

    @staticmethod
    def store_advise_model_in_db(model, scaler_X, scaler_y, accuracy):
        database = Database()
        database.create_table(CREATE_ADVISE_MODEL_QUERY)
        database.drop_table(DELETE_ALL_ADVISE_MODELS_QUERY)
        pickled_tuple = ModelStorage.__get_tuple_pickled((model, scaler_X, scaler_y))
        database.insert_data(INSERT_ADVISE_MODEL_QUERY, (*pickled_tuple, accuracy))
        database.close_connection()

    @staticmethod
    def get_main_model_from_db():
        database = Database()
        get_data = database.fetch_all_data(GET_MODEL_QUERY)[0]
        print(get_data)
        database.close_connection()
        unpickled_model = ModelStorage.__get_unpickled(get_data[1])
        unpickled_scalers_tuple = ModelStorage.__get_tuple_unpickled((get_data[2], get_data[3]))
        return unpickled_model, unpickled_scalers_tuple

    @staticmethod
    def get_advise_model_from_db():
        database = Database()
        get_data = database.fetch_all_data(GET_ADVISE_MODEL_QUERY)[0]
        database.close_connection()
        unpickled_model = ModelStorage.__get_unpickled(get_data[1])
        unpickled_scalers_tuple = ModelStorage.__get_tuple_unpickled((get_data[2], get_data[3]))
        return unpickled_model, unpickled_scalers_tuple, get_data[4]

    @staticmethod
    def count_advise_items():
        database = Database()
        database.create_table(CREATE_ADVICE_TABLE_QUERY)
        counter = database.fetch_all_data(GET_ITEMS_COUNTER_QUERY)[0][0]
        database.close_connection()
        return counter
