from server.database.database import Database
import pickle
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))


class ModelStorage:
    @staticmethod
    def __store_pickle(obj, file_name):
        with open(f'{curr_dir}/pickle_files/{file_name}.pickle', 'wb') as bin_file:
            pickle.dump(obj, bin_file)

    @staticmethod
    def __get_pickle(file_name):
        with open(f'{curr_dir}/pickle_files/{file_name}.pickle', 'rb') as bin_file:
            obj = pickle.load(bin_file)
        return obj

    @staticmethod
    def store_model_in_db(model, encoders, scaler_X, scaler_y):
        ModelStorage.__store_pickle(model, 'model')
        ModelStorage.__store_pickle(encoders, 'encoders')
        ModelStorage.__store_pickle(scaler_X, 'scaler_X')
        ModelStorage.__store_pickle(scaler_y, 'scaler_y')

    @staticmethod
    def get_model_from_db():
        model = ModelStorage.__get_pickle('model')
        encoders = ModelStorage.__get_pickle('encoders')
        scaler_X = ModelStorage.__get_pickle('scaler_X')
        scaler_y = ModelStorage.__get_pickle('scaler_y')

        return model, (encoders, scaler_X, scaler_y)
