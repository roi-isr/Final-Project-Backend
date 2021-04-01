from server.ML.Algorithms.ML_utility import *
import pandas as pd
from sqlalchemy import create_engine
from server.database.queries.admin_price_advice import GET_ADVISE_ALL_QUERY


def read_data():
    db_engine = create_engine("postgresql://srmngikqacnqlj:c74259d2a98acc497a45815abd47dfd4cf0d29484019b547d1c1b8fe789f9fd2@ec2-54-170-100-209.eu-west-1.compute.amazonaws.com:5432/d6sja18bu5d6qh")
    dataframe = pd.read_sql_query(GET_ADVISE_ALL_QUERY, db_engine)
    return dataframe


def build_and_test_regression_models():
    diamond_dataset = read_data()
    regressor = RegressionCustom(diamond_dataset)
    regressor.pre_processing()
    regressor.run_algorithms()
    # Return the model itself
    return regressor.max_accuracy_model[0], regressor.scaler_X, regressor.scaler_y, regressor.max_accuracy_model[1]


# Make some predictions (up to the user) over the best selected model
def make_predictions(best_regression_model, scalers, user_features):
    # Making a prediction out of the best chosen model
    predicted_result = RegressionCustom.predict_result(best_regression_model, *scalers, [user_features])
    return predicted_result

