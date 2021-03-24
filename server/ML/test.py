
# THIS PROGRAM MAY DONE EXECUTING IN UP TO 30 MINUTE (MAKING SOME HEAVY CALCULATIONS)

# Importing the diamond_regression '.py' file
from .diamond_regressions import build_and_test_regression_models, make_predictions

# Main scope
if __name__ == '__main__':

    # Building and testing the regression models over the diamonds dataset
    best_regression_model = build_and_test_regression_models()

    # Make some predictions (up to the user) over the best selected model
    make_predictions(best_regression_model)
