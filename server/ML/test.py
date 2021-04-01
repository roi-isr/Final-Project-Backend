# THIS PROGRAM MAY DONE EXECUTING IN UP TO 30 MINUTE (MAKING SOME HEAVY CALCULATIONS)

# Importing the diamond_regression '.py' file
from server.ML.diamond_regressions import build_and_test_regression_models, make_predictions
from server.ML.model_storage import ModelStorage


def build_ml_models():
    # Building and testing the regression models over the diamonds dataset
    best_regression_model, features_ranks, scaler_X, scaler_y = build_and_test_regression_models()
    ModelStorage.store_model_in_db(best_regression_model, scaler_X, scaler_y)


def exec_predictions(data_list):
    # Make some predictions (up to the user) over the best selected model
    try:
        best_regression_model, scalers = ModelStorage.get_model_from_db()
        predicted_price = make_predictions(best_regression_model, scalers, data_list)
        return predicted_price
    except:
        print("\nInvalid data entered. Please enter data again.")
