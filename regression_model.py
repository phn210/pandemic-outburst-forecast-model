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

def predict(input_file_path, x):
    df_orig = pd.read_csv(input_file_path, on_bad_lines='skip')
    df = copy.deepcopy(df_orig)
    # print(df)

    days_since_lst = []
    length = len(df_orig)
    for i in range(length):
        days_since_lst.append(i)

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

    head, tail = os.path.split(input_file_path)
    file_name = "Predict_for_" + tail
    output_file_path = head + "/" + file_name

    df_output = pd.DataFrame()
    df_output['predict_confirmed_case'] = linear_pred
    for i in range(x):
        X_train = numpy.append(X_train, 0)
    df_output['confirmed_case'] = X_train
    # df_output.to_csv(output_file_path)
    print(df_output)
    return df_output


predict("data/VN-covid19.csv", 14)