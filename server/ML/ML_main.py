# THIS PROGRAM MAY DONE EXECUTING IN UP TO 30 MINUTE (MAKING SOME HEAVY CALCULATIONS)

# Importing the diamond_regression '.py' file
from server.ML.diamond_regressions import \
    build_and_test_regression_models as build_diamond_regression, \
    make_predictions as make_diamond_predictions
from server.ML.price_advise_regressions import \
    build_and_test_regression_models as build_advise_regression, \
    make_predictions as make_advise_predictions
from server.ML.sells_regressions import \
    build_and_test_regression_models as build_sells_regression, \
    make_predictions as make_sells_predictions
from server.ML.Storage.model_storage import ModelStorage
import math


def build_ml_models():
    # Building and testing the regression models over the diamonds dataset
    best_regression_model, features_ranks, scaler_X, scaler_y = build_diamond_regression()
    ModelStorage.store_main_model_in_db(best_regression_model, scaler_X, scaler_y)


def build_ml_advise_models():
    if ModelStorage.count_advise_items() > 7:
        # Building and testing the regression models over the diamonds dataset
        best_regression_model, scaler_X, scaler_y, accuracy = build_advise_regression()
        ModelStorage.store_advise_model_in_db(best_regression_model, scaler_X, scaler_y, accuracy)


def build_ml_sells_models():
    if ModelStorage.count_sell_items() > 7:
        # Building and testing the regression models over the diamonds dataset
        best_regression_model, scaler_X, scaler_y, accuracy = build_sells_regression()
        ModelStorage.store_sells_model_in_db(best_regression_model, scaler_X, scaler_y, accuracy)


def calc_advise_result_influence(data_list, num_of_advice_items, predicted_price):
    best_advise_regression_model, scalers_advise, accuracy = ModelStorage.get_advise_model_from_db()
    print(F'---------COUNTER: {ModelStorage.count_advise_items()}, PRED: {accuracy}---------------')
    predicted_advise_price = make_advise_predictions(best_advise_regression_model, scalers_advise, data_list)
    if accuracy > 0:
        experience_rank = (math.atan(0.05 * num_of_advice_items) / math.pi) * 2
        admin_expertise = accuracy * experience_rank
    else:
        admin_expertise = 0
    advise_pred = (admin_expertise * predicted_advise_price) + ((1 - admin_expertise) * predicted_price)
    return advise_pred, admin_expertise


def calc_sells_result_influence(data_list, num_of_sells_items, predicted_price):
    best_sells_regression_model, scalers_sells, accuracy = ModelStorage.get_sells_model_from_db()
    print(F'---------COUNTER: {ModelStorage.count_sell_items()}, PRED: {accuracy}---------------')
    predicted_sells_price = make_sells_predictions(best_sells_regression_model, scalers_sells, data_list)
    print(f'sells_pred {predicted_sells_price}')

    print(f'acc: {accuracy}')
    if accuracy > 0:
        experience_rank = (math.atan(0.05 * num_of_sells_items) / math.pi) * 2
        admin_expertise = accuracy * experience_rank
    else:
        admin_expertise = 0
    sells_pred = (admin_expertise * predicted_sells_price) + ((1 - admin_expertise) * predicted_price)
    return sells_pred, admin_expertise


def exec_predictions(data_list):
    # Make some predictions (up to the user) over the best selected model
    # try:
    num_of_advice_items = ModelStorage.count_advise_items()
    num_of_sells_items = ModelStorage.count_sell_items()
    best_main_regression_model, scalers_main = ModelStorage.get_main_model_from_db()
    predicted_price = make_diamond_predictions(best_main_regression_model, scalers_main, data_list)

    if num_of_advice_items > 7:
        advise_pred, advise_exp = calc_advise_result_influence(data_list, num_of_advice_items, predicted_price)
    else:
        advise_pred = predicted_price
        advise_exp = 0

    if num_of_sells_items > 7:
        sells_pred, sells_exp = calc_sells_result_influence(data_list, num_of_sells_items, predicted_price)
    else:
        sells_pred = predicted_price
        sells_exp = 0

    if advise_exp == 0 and sells_exp == 0:
        final_pred = predicted_price
    else:
        # Calculate the weighted average between the two models
        final_pred = (advise_pred * advise_exp + sells_pred * sells_exp) / (advise_exp + sells_exp)
    print(f'pred {predicted_price}')
    return "{:,.1f}$".format(final_pred)
    # except:
    #     print("\nInvalid data entered. Please enter data again.")

build_ml_sells_models()
build_ml_advise_models()