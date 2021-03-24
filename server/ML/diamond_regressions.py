import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressors
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.feature_selection import SelectKBest

global scaler_X, scaler_y, encoders


# Read relevant data from 'diamonds.csv' file
def read_data():
    # Reading the data from the 'diamonds.csv' file
    dataset = pd.read_csv('../Data/diamonds.csv')
    # Taking the relevant features from the CSV data
    dataset = dataset.iloc[:, [1, 2, 3, 4, 5, 6, -1]]
    return dataset


# Run a collection of regression model and find the best model, considering test accuracy
def run_algorithms(X_train, X_test, X_test_origin, y_train, y_test):
    models_list = [
        run_linear_regression(X_train, X_test, X_test_origin, y_train, y_test),
        run_polynomial_regression(X_train, X_test, X_test_origin, y_train, y_test),
        run_svm_regression(X_train, X_test, X_test_origin, y_train, y_test),
        run_decision_tree_regression(X_train, X_test, X_test_origin, y_train, y_test),
        run_random_forest_regression(X_train, X_test, X_test_origin, y_train, y_test),
        run_adaboost_regression(X_train, X_test, X_test_origin, y_train, y_test)
    ]
    max_accuracy_model = max(models_list, key=lambda model: model[1])
    print("""
==================================================================================
The optimal accuracy model is {}, with {:.4f}% of accuracy
==================================================================================
"""
          .format(max_accuracy_model[2],
                  max_accuracy_model[1] * 100))

    return max_accuracy_model


# Print the K best features of the dataset
def print_best_features(diamond_dataset, feature_selected_index_list):
    best_feature_names = list(diamond_dataset.columns[feature_selected_index_list])
    print("The best feature{} {}: {}.\n".format('s' if len(feature_selected_index_list) > 1 else '',
                                                'are' if len(feature_selected_index_list) > 1 else 'is',
                                                ', '.join(best_feature_names)))


# Find the best k features of the dataset, then run a various regression model in order to find the best model for
# those features
def k_best_features_exec(diamond_dataset, k_attr):
    X_train, X_test, y_train, y_test = pre_processing(diamond_dataset)
    best_attr_processor = SelectKBest(k=k_attr)
    X_train_new = best_attr_processor.fit_transform(X_train, y_train)
    X_test_new = best_attr_processor.transform(X_test)
    # Find best features indexes
    feature_selected_index_list = [chosen_index
                                   for chosen_index, i in enumerate(best_attr_processor.get_support().astype(int))
                                   if i == 1]
    # Keeping the origin X_test dataset (not standardized), for later visualization purpose
    X_test_origin = scaler_X.inverse_transform(X_test)[:, feature_selected_index_list]
    print_best_features(diamond_dataset, feature_selected_index_list)
    max_accuracy_model = run_algorithms(X_train_new, X_test_new, X_test_origin, y_train, y_test)
    return max_accuracy_model


# Normalizing data
def normalize_data(X_train, X_test, y_train, y_test):
    global scaler_X, scaler_y
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)
    scaler_y = StandardScaler()
    y_train = scaler_y.fit_transform(y_train)
    y_test = scaler_y.transform(y_test)
    return X_train, X_test, y_train, y_test


# Encoding classes (categorical data) to integers, beginning from 0 - dealing with categorical data
def encode_data(X_train, X_test):
    global encoders
    encoders = {i: LabelEncoder() for i in range(1, 4)}
    # Marking the categorical data
    categorical_data_indexes = [1, 2, 3]
    for data_index in categorical_data_indexes:
        curr_categorical_train_data = X_train[:, data_index]
        X_train[:, data_index] = encoders[data_index].fit_transform(curr_categorical_train_data)
        curr_categorical_test_data = X_test[:, data_index]
        X_test[:, data_index] = encoders[data_index].transform(curr_categorical_test_data)
    return X_train, X_test


# Preprocessing the data before building the model, includes - splitting the data
# into train and test sets, normalizing and encoding categorical data.
def pre_processing(dataset):
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    y = y.reshape(len(y), 1)

    # Split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    X_train, X_test = encode_data(X_train, X_test)

    X_train, X_test, y_train, y_test = normalize_data(X_train, X_test, y_train, y_test)

    return X_train, X_test, y_train.ravel(), y_test.ravel()


# Calculating test accuracy
def calc_test_accuracy(y_test, y_pred):
    accuracy = r2_score(y_test, y_pred)
    return accuracy


# Calculating cross validation accuracy (in order to prevent over-fitting)
def apply_cross_validation(regressor, X_train, y_train, cv):
    accuracies = cross_val_score(estimator=regressor, X=X_train, y=y_train, cv=cv)
    return accuracies.mean()


# Run linear regression model
def run_linear_regression(X_train, X_test, X_test_origin, y_train, y_test):
    linear_regressor = LinearRegression()
    # Train the model on the train set
    linear_regressor.fit(X_train, y_train)
    y_pred = scaler_y.inverse_transform(linear_regressor.predict(X_test))
    test_accuracy = calc_test_accuracy(y_test=scaler_y.inverse_transform(y_test), y_pred=y_pred)
    cv_accuracy = apply_cross_validation(linear_regressor, X_train, y_train, cv=10)
    avg_accuracy = (test_accuracy + cv_accuracy) / 2
    print("The accuracy score of the linear regression is: {:.4f}%".format(avg_accuracy * 100))
    # If the model was built on one attribute only, draw a visual graph

    return linear_regressor, avg_accuracy, "Linear Regression"


# Run polynomial regression model - with degrees of 2, 3, and 4 respectively
def run_polynomial_regression(X_train, X_test, X_test_origin, y_train, y_test):
    model_test_degrees = [2, 3, 4]
    polynomial_model_list = []
    for curr_degree in model_test_degrees:
        polynomial_regressor = PolynomialFeatures(degree=curr_degree)
        # Build a polynomial model
        X_poly = polynomial_regressor.fit_transform(X_train)
        linear_regressor = LinearRegression()
        # Train the model on train set
        linear_regressor.fit(X_poly, y_train)
        y_pred = scaler_y.inverse_transform(linear_regressor.predict(polynomial_regressor.transform(X_test)))
        test_accuracy = calc_test_accuracy(y_test=scaler_y.inverse_transform(y_test), y_pred=y_pred)
        cv_accuracy = apply_cross_validation(linear_regressor, X_train, y_train, cv=10)
        avg_accuracy = (test_accuracy + cv_accuracy) / 2
        print("The accuracy score of the polynomial regression with {} degree is: {:.4f}%".format(curr_degree,
                                                                                                  avg_accuracy * 100))
        polynomial_model_list.append(
            (linear_regressor, avg_accuracy, "{} Degree Polynomial Regression".format(curr_degree)))
        # If the model was built on one attribute only, draw a visual graph

    # Return the best fitting model (degree)
    return max(polynomial_model_list, key=lambda model: model[1])


# Run SVM (Support Vector Machine) regression model
def run_svm_regression(X_train, X_test, X_test_origin, y_train, y_test):
    # Build a SVM model with the 'rbf' kernel
    svm_regressor = SVR(kernel='rbf')
    # Train the model on train set
    svm_regressor.fit(X_train, y_train)
    y_pred = scaler_y.inverse_transform(svm_regressor.predict(X_test))
    test_accuracy = calc_test_accuracy(y_test=scaler_y.inverse_transform(y_test), y_pred=y_pred)
    cv_accuracy = apply_cross_validation(svm_regressor, X_train, y_train, cv=3)
    avg_accuracy = (test_accuracy + cv_accuracy) / 2
    print("The accuracy score of the polynomial regression with SVM regression is: {:.4f}%".format(avg_accuracy * 100))
    # If the model was built on one attribute only, draw a visual graph

    return svm_regressor, avg_accuracy, "SVM Regression"


# Run decision tree regression model
def run_decision_tree_regression(X_train, X_test, X_test_origin, y_train, y_test):
    # Build the model with 'best' model - with considers all of the attributes in the calculation
    decision_tree_regressor = DecisionTreeRegressor(random_state=42, splitter='best')
    # Train the model on the train set
    decision_tree_regressor.fit(X_train, y_train)
    # Predict the results on the test set
    y_pred = scaler_y.inverse_transform(decision_tree_regressor.predict(X_test))
    test_accuracy = calc_test_accuracy(y_test=scaler_y.inverse_transform(y_test), y_pred=y_pred)
    cv_accuracy = apply_cross_validation(decision_tree_regressor, X_train, y_train, cv=10)
    avg_accuracy = (test_accuracy + cv_accuracy) / 2
    print("The accuracy score of the polynomial regression with decision tree is: {:.4f}%".format(avg_accuracy * 100))
    # If the model was built on one attribute only, draw a visual graph

    return decision_tree_regressor, avg_accuracy, "Decision Tree Regression"


# Run random forest regression model - combines multiple trees based on sub-features and sub-samples, then takes the
# average of all
def run_random_forest_regression(X_train, X_test, X_test_origin, y_train, y_test):
    # Parameters of the model - the number of trees to build (estimators)
    model_params = {'n_estimators': [10, 50, 100]}
    random_forest_regressor = RandomForestRegressor(random_state=42)
    grid_search_random_forest_regressor = GridSearchCV(random_forest_regressor, model_params)
    # Train the best parameter's model (found by grid search algorithm) on the train set
    grid_search_random_forest_regressor.fit(X_train, y_train)
    y_pred = scaler_y.inverse_transform(grid_search_random_forest_regressor.predict(X_test))
    test_accuracy = calc_test_accuracy(y_test=scaler_y.inverse_transform(y_test), y_pred=y_pred)
    cv_accuracy = apply_cross_validation(grid_search_random_forest_regressor, X_train, y_train, cv=5)
    avg_accuracy = (test_accuracy + cv_accuracy) / 2
    best_param = grid_search_random_forest_regressor.best_params_['n_estimators']
    print("The accuracy score of the polynomial regression with random forest is: {:.4f}%".format(avg_accuracy * 100))
    # If the model was built on one attribute only, draw a visual graph

    return grid_search_random_forest_regressor, avg_accuracy, "Random Forest Regression"


# run adaboost regression with 10 expertises - default is decision tree with maximum depth of 3
def run_adaboost_regression(X_train, X_test, X_test_origin, y_train, y_test):
    model_params = {'learning_rate': [0.1, 1, 10]}
    adaboost_regressor = AdaBoostRegressor(random_state=42, n_estimators=20, learning_rate=0.1)
    grid_search_adaboost_regressor = GridSearchCV(adaboost_regressor, model_params)
    # Train the model on the train set
    grid_search_adaboost_regressor.fit(X_train, y_train)
    # Predict test results
    y_pred = scaler_y.inverse_transform(grid_search_adaboost_regressor.predict(X_test))
    test_accuracy = calc_test_accuracy(y_test=scaler_y.inverse_transform(y_test), y_pred=y_pred)
    cv_accuracy = apply_cross_validation(grid_search_adaboost_regressor, X_train, y_train, cv=5)
    avg_accuracy = (test_accuracy + cv_accuracy) / 2
    best_param = grid_search_adaboost_regressor.best_params_['learning_rate']
    print("The accuracy score of the polynomial regression with adaboost regression is: {:.4f}%".format(
        avg_accuracy * 100))
    # If the model was built on one attribute only, draw a visual graph

    return grid_search_adaboost_regressor, avg_accuracy, "Adaboost Regression"


def build_and_test_regression_models():
    diamond_dataset = read_data()
    accuracy_list = []
    final_model = None
    attributes_count = diamond_dataset.shape[1] - 1
    # Go through all num amounts of best attrs (1 to 6)
    for num_of_attrs in range(1, attributes_count + 1):
        print("\n---------------------{} Attribute{} Models---------------------\n".format(num_of_attrs,
                                                                                           's' if num_of_attrs > 1
                                                                                           else ''))
        # Find best K features model, and the build and run the various regression model, in order to predict
        # diamonds prices
        max_accuracy_model = k_best_features_exec(diamond_dataset, num_of_attrs)
        # Keep the last model (6 features) to predictions
        if num_of_attrs == 6:
            final_model = max_accuracy_model[0]
        accuracy_list.append(max_accuracy_model[1])

    return final_model


# Get a sample data from the user (as an input), and predict the price of the diamond
def predict_result(regression_model, data):
    new_data = np.array(data.copy())
    # Encoding input data
    categorical_data_indexes = [1, 2, 3]
    for data_index in categorical_data_indexes:
        curr_categorical_train_data = new_data[:, data_index]
        new_data[:, data_index] = encoders[data_index].transform(curr_categorical_train_data)
    # Normalizing input data
    normalized_data = scaler_X.transform(new_data)
    predicted_price = scaler_y.inverse_transform(regression_model.predict(normalized_data))
    # Return formatted price with separated commas and a dollar sign ('$')
    return "{:,}$".format(int(predicted_price[0]))


# Make some predictions (up to the user) over the best selected model
def make_predictions(best_regression_model):
    # The diamonds features list, for later input from the user
    features_list = ['weight in carat', 'cut', 'color', 'clarity', 'depth', 'table']

    print("----------MAKE SOME PREDICTIONS!----------")

    while True:
        # Getting the feature as an input from the user, for later best model's prediction
        user_features = []

        for i in range(0, 6):
            new_feature = input("\nPlease enter the {}:\n".format(features_list[i]))
            user_features.append(new_feature)

        try:
            # Making a prediction out of the best chosen model
            predicted_result = predict_result(best_regression_model,
                                              [user_features])
        except:
            print("\nInvalid data entered. Please enter data again.")
            continue

        # Printing the predicted result
        print("""
===========================================================================
The predicted price of the given diamond is: {}
===========================================================================
"""
              .format(predicted_result))

        # Make more predictions (optional)
        while True:
            more_predictions = input("\nMake more predictions? (Y/N): ")

            if more_predictions == 'Y' or more_predictions == 'N':
                break
            else:
                print("\nInvalid value entered")

        if more_predictions == 'Y':
            continue
        else:
            print("\nThank you and goodbye!")
            break
