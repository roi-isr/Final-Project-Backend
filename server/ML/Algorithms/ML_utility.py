import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_selection import SelectKBest

labels = [{
    'Fair': 0,
    'Ideal': 1,
    'Good': 2,
    'Very Good': 3,
    'Premium': 4
},
{
    'Z': 0,
    'N': 1,
    'K': 2,
    'J': 3,
    'I': 4,
    'H': 5,
    'G': 6,
    'F': 7,
    'E': 8,
    'D': 9
},
{
    'I3': 0,
    'I2': 1,
    'I1': 2,
    'SI2': 3,
    'SI1': 4,
    'VS2': 5,
    'VS1': 6,
    'VVS2': 7,
    'VVS1': 8,
    'IF': 9,
    'FL': 10
}]

class RegressionCustom:
    def __init__(self, dataset):
        print("Starting regression process...")
        self.dataset = dataset
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.scaler_X = None
        self.scaler_y = None
        self.max_accuracy_model = None

    # Run a collection of regression model and find the best model, considering test accuracy
    def run_algorithms(self):
        models_list = [
            self.run_linear_regression(),
            self.run_decision_tree_regression(),
            self.run_random_forest_regression()
        ]
        self.max_accuracy_model = max(models_list, key=lambda model: model[1])
        print("""
    ==================================================================================
    The optimal accuracy model is {}, with {:.4f}% of accuracy
    ==================================================================================
    """
              .format(self.max_accuracy_model[2],
                      self.max_accuracy_model[1] * 100))

        return self.max_accuracy_model

    # Find the best k features of the dataset, then run a various regression model in order to find the best model for
    # those features
    def k_best_features_exec(self, column_names_list, k_attr):
        best_attr_processor = SelectKBest(k=k_attr)
        best_attr_processor.fit_transform(self.X_train, self.y_train)
        for i, j in sorted(zip(column_names_list, best_attr_processor.scores_), key=lambda x: x[1], reverse=True):
            print(f'{i}: {j}')
        return sorted(zip(column_names_list, best_attr_processor.scores_), key=lambda x: x[1], reverse=True)

    # Normalizing data
    def normalize_data(self):
        self.scaler_X = StandardScaler()
        self.X_train = self.scaler_X.fit_transform(self.X_train)
        self.X_test = self.scaler_X.transform(self.X_test)
        self.scaler_y = StandardScaler()
        self.y_train = self.scaler_y.fit_transform(self.y_train)
        self.y_test = self.scaler_y.transform(self.y_test)

    # Encoding classes (categorical data) to integers, beginning from 0 - dealing with categorical data
    def encode_data(self):
        # Marking the categorical data
        categorical_data_indexes = [1, 2, 3]
        for data_index in categorical_data_indexes:
            self.X_train[:, data_index] = np.array([labels[data_index-1][i] for i in self.X_train[:, data_index]])
            self.X_test[:, data_index] = np.array([labels[data_index-1][i] for i in self.X_test[:, data_index]])

    # Preprocessing the data before building the model, includes - splitting the data
    # into train and test sets, normalizing and encoding categorical data.
    def pre_processing(self):
        X = self.dataset.iloc[:, :-1].values
        y = self.dataset.iloc[:, -1].values
        y = y.reshape(len(y), 1)

        # Split the dataset into train and test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        self.encode_data()

        self.normalize_data()

        self.y_train, self.y_test = self.y_train.ravel(), self.y_test.ravel()

    # Calculating test accuracy
    def calc_test_accuracy(self, y_test, y_pred):
        accuracy = r2_score(y_test, y_pred)
        return accuracy

    # Calculating cross validation accuracy (in order to prevent over-fitting)
    def apply_cross_validation(self, regressor, cv):
        accuracies = cross_val_score(estimator=regressor, X=self.X_train, y=self.y_train, cv=cv)
        return accuracies.mean()

    # Run linear regression model
    def run_linear_regression(self):
        linear_regressor = LinearRegression()
        # Train the model on the train set
        linear_regressor.fit(self.X_train, self.y_train)
        y_pred = self.scaler_y.inverse_transform(linear_regressor.predict(self.X_test))
        test_accuracy = self.calc_test_accuracy(y_test=self.scaler_y.inverse_transform(self.y_test), y_pred=y_pred)
        if len(self.X_train) > 20:
            cv_accuracy = self.apply_cross_validation(linear_regressor, cv=10)
            avg_accuracy = (test_accuracy + cv_accuracy) / 2
        else:
            avg_accuracy = test_accuracy
        print("The accuracy score of the linear regression is: {:.4f}%".format(avg_accuracy * 100))
        return linear_regressor, avg_accuracy, "Linear Regression"

    # Run decision tree regression model
    def run_decision_tree_regression(self):
        # Build the model with 'best' model - with considers all of the attributes in the calculation
        decision_tree_regressor = DecisionTreeRegressor(random_state=42, splitter='best')
        # Train the model on the train set
        decision_tree_regressor.fit(self.X_train, self.y_train)
        # Predict the results on the test set
        y_pred = self.scaler_y.inverse_transform(decision_tree_regressor.predict(self.X_test))
        test_accuracy = self.calc_test_accuracy(y_test=self.scaler_y.inverse_transform(self.y_test), y_pred=y_pred)
        if len(self.X_train) > 20:
            cv_accuracy = self.apply_cross_validation(decision_tree_regressor, cv=10)
            avg_accuracy = (test_accuracy + cv_accuracy) / 2
        else:
            avg_accuracy = test_accuracy
        print("The accuracy score of the regression with decision tree is: {:.4f}%".format(avg_accuracy * 100))
        return decision_tree_regressor, avg_accuracy, "Decision Tree Regression"

    # Run random forest regression model - combines multiple trees based on sub-features and sub-samples, then takes the
    # average of all
    def run_random_forest_regression(self):
        # Parameters of the model - the number of trees to build (estimators)
        random_forest_regressor = RandomForestRegressor(random_state=42, n_estimators=20)
        # Train the best parameter's model (found by grid search algorithm) on the train set
        random_forest_regressor.fit(self.X_train, self.y_train)
        y_pred = self.scaler_y.inverse_transform(random_forest_regressor.predict(self.X_test))
        test_accuracy = self.calc_test_accuracy(y_test=self.scaler_y.inverse_transform(self.y_test), y_pred=y_pred)
        if len(self.X_train) > 20:
            cv_accuracy = self.apply_cross_validation(random_forest_regressor, cv=5)
            avg_accuracy = (test_accuracy + cv_accuracy) / 2
        else:
            avg_accuracy = test_accuracy
        print("The accuracy score of the polynomial with random forest is: {:.4f}%".format(avg_accuracy * 100))
        return random_forest_regressor, avg_accuracy, "Random Forest Regression"

    @staticmethod
    # Get a sample data from the user (as an input), and predict the price of the diamond
    def predict_result(regression_model, scaler_X_arg, scaler_y_arg, data):
        new_data = np.array(data.copy())
        # Encoding input data
        categorical_data_indexes = [1, 2, 3]
        for data_index in categorical_data_indexes:
            curr_categorical_train_data = new_data[:, data_index]
            new_data[:, data_index] = labels[data_index-1][new_data[:, data_index][0]]
        # Normalizing input data
        normalized_data = scaler_X_arg.transform(new_data)
        predicted_price = scaler_y_arg.inverse_transform(regression_model.predict(normalized_data))
        # Return formatted price with separated commas and a dollar sign ('$')
        return int(predicted_price[0])
