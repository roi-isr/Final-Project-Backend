from server.ML.ML_utility import *
import pandas as pd
import os


# Read relevant data from 'diamonds.csv' file
def read_data():
    # Reading the data from the 'diamonds.csv' file
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    dataset = pd.read_csv(f'{curr_dir}/Data/diamonds.csv')
    # Taking the relevant features from the CSV data
    dataset = dataset.iloc[:, [1, 2, 3, 4, 5, 6, -1]]
    return dataset


def build_and_test_regression_models():
    diamond_dataset = read_data()
    regressor = RegressionCustom(diamond_dataset)
    regressor.pre_processing()
    features_ranks = regressor.k_best_features_exec(diamond_dataset.columns, 6)
    regressor.run_algorithms()
    # Return the model itself
    return regressor.max_accuracy_model[0], features_ranks, regressor.scaler_X, regressor.scaler_y


# Make some predictions (up to the user) over the best selected model
def make_predictions(best_regression_model, scalers, user_features):
    # Making a prediction out of the best chosen model
    predicted_result = RegressionCustom.predict_result(best_regression_model, *scalers, [user_features])
    return predicted_result
