
# THIS PROGRAM MAY DONE EXECUTING IN UP TO 30 MINUTE (MAKING SOME HEAVY CALCULATIONS)

# Importing the diamond_regression '.py' file
from server.ML.diamond_regressions import build_and_test_regression_models, make_predictions


def exec_predictions(data_list):
    # Building and testing the regression models over the diamonds dataset
    best_regression_model, features_ranks = build_and_test_regression_models()

    # Make some predictions (up to the user) over the best selected model
    try:
        predicted_price = make_predictions(best_regression_model, data_list)
        return predicted_price
    except:
        print("\nInvalid data entered. Please enter data again.")
