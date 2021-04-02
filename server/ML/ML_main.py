# THIS PROGRAM MAY DONE EXECUTING IN UP TO 30 MINUTE (MAKING SOME HEAVY CALCULATIONS)

# Importing the diamond_regression '.py' file
from server.ML.diamond_regressions import \
    build_and_test_regression_models as build_diamond_regression, \
    make_predictions as make_diamond_predictions
from server.ML.price_advise_regression import \
    build_and_test_regression_models as build_advise_regression, \
    make_predictions as make_advise_predictions
from server.ML.Storage.model_storage import ModelStorage
import math


def build_ml_models():
    # Building and testing the regression models over the diamonds dataset
    best_regression_model, features_ranks, scaler_X, scaler_y = build_diamond_regression()
    ModelStorage.store_main_model_in_db(best_regression_model, scaler_X, scaler_y)


def build_ml_advise_models():
    print(ModelStorage.count_advise_items())
    if ModelStorage.count_advise_items() > 7:
        # Building and testing the regression models over the diamonds dataset
        best_regression_model, scaler_X, scaler_y, accuracy = build_advise_regression()
        ModelStorage.store_advise_model_in_db(best_regression_model, scaler_X, scaler_y, accuracy)


def exec_predictions(data_list):
    # Make some predictions (up to the user) over the best selected model
    # try:
    num_of_items = ModelStorage.count_advise_items()
    best_main_regression_model, scalers_main = ModelStorage.get_main_model_from_db()
    predicted_price = make_diamond_predictions(best_main_regression_model, scalers_main, data_list)
    if num_of_items > 7:
        best_advise_regression_model, scalers_advise, accuracy = ModelStorage.get_advise_model_from_db()
        print(F'---------COUNTER: {ModelStorage.count_advise_items()}, PRED: {accuracy}---------------')
        predicted_advise_price = make_advise_predictions(best_advise_regression_model, scalers_advise, data_list)
        if accuracy > 0:
            experience_rank = (math.atan(0.05 * num_of_items)/math.pi) * 2
            admin_expertise = accuracy * experience_rank
        else:
            admin_expertise = 0
        final_pred = (admin_expertise * predicted_advise_price) + ((1 - admin_expertise) * predicted_price)
    else:
        final_pred = predicted_price

    return "{:,.1f}$".format(final_pred)
    # except:
    #     print("\nInvalid data entered. Please enter data again.")
