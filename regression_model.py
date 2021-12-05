import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import ntpath
import os
from sklearn.pipeline import make_pipeline

# Đầu vào là Pandas dataframe có 2 column là 'ObservationDate' và 'Confirmed'
def predict(df, x):
    # df = pd.read_csv(input_file_path, on_bad_lines='skip')
    # df = copy.deepcopy(df_orig)
    # print(df['ObservationDate'])

    days_since_lst = []
    length = len(df)
    for i in range(length):
        days_since_lst.append(i)

    date = np.array(df['ObservationDate'])
    X_train = np.array(df["Confirmed"])  # .reshape(-1,1)
    # X is the world cases array
    y_train = np.array(days_since_lst).reshape(-1, 1)

    for i in range(length, length + x):
        days_since_lst.append(i)
    y = np.array(days_since_lst).reshape(-1, 1)

    days_since_lst = []
    for i in range(length, length + x):
        days_since_lst.append(i)

    y_test = np.array(days_since_lst).reshape(-1, 1)

    poly = PolynomialFeatures(degree=6)
    poly_y_train = poly.fit_transform(y_train)
    poly_y_test = poly.fit_transform(y_test)
    poly_y = poly.fit_transform(y)

    linear_model = LinearRegression(normalize=True, fit_intercept=False)
    linear_model.fit(poly_y_train, X_train)
    test_linear_pred = linear_model.predict(poly_y_test)
    linear_pred = linear_model.predict(poly_y)

    # print(linear_pred)
    # print(test_linear_pred)


    plt.style.use("dark_background")
    plt.figure(figsize=(15, 10))
    plt.plot(y,
             linear_pred,
             label='Polynomial Regression Prediction of Future Cases',
             linestyle="dashed",
             color='gold')

    plt.plot(y_train,
             X_train,
             label='Training Cases',
             color='lightgrey')

    plt.xlabel('Days Since', size=30)
    plt.ylabel('# of Cases', size=30)
    plt.legend()
    plt.xticks(size=30)
    plt.yticks(size=30)
    plt.show()

    # head, tail = os.path.split(input_file_path)
    file_name = "Predict_result.csv"
    output_file_path = "./data/" + file_name

    df_output = pd.DataFrame()

    for i in range(linear_pred.size):
        linear_pred[i] = round(linear_pred[i])
    df_output['predict_confirmed_case'] = linear_pred

    for i in range(x):
        X_train = numpy.append(X_train, 0)
        date = numpy.append(date, 'Null')

    df_output['confirmed_case'] = X_train
    df_output['observation_date'] = date

    df_output.to_csv(output_file_path)

    print(df_output)

df = pd.read_csv("data/VN-covid19.csv", on_bad_lines='skip')
predict(df, 14)