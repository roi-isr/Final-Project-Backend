import pandas as pd
from sqlalchemy import create_engine

from server.ML.Algorithms.ML_utility import *
from server.database.queries.ML_sells import GET_SELLS_DATA_QUERY
from server.config.connection_config import DATABASE_URL


def read_data():
    db_engine = create_engine(DATABASE_URL)
    dataframe = pd.read_sql_query(GET_SELLS_DATA_QUERY, db_engine)
    return dataframe


def build_and_test_regression_models():
    sells_dataset = read_data()
    print(sells_dataset)
    regressor = RegressionCustom(dataset=sells_dataset)
    regressor.pre_processing(labeled_indexes=[1, 2])
    regressor.run_algorithms()
    # Return the model itself
    return regressor.max_accuracy_model[0], regressor.scaler_X, regressor.scaler_y, regressor.max_accuracy_model[1]


# Make some predictions (up to the user) over the best selected model
def make_predictions(best_regression_model, scalers, user_features):
    # Making a prediction out of the best chosen model
    predicted_result = RegressionCustom.predict_result(best_regression_model, *scalers, [[user_features[i]
                                                                                          for i in [0, 2, 3]]],
                                                       [1, 2])
    return predicted_result

# a = read_data()
# print(a)
