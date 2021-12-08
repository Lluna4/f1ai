import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import csv

data = pd.read_csv("data.csv", usecols=[0, 1, 2, 3, 4, 5])
td = pd.read_csv("data.csv", usecols=[0, 1, 2, 4, 5])




pred = " fldeg"

X = np.array(data.drop([pred], 1))
y = np.array(data[pred])
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
linear = linear_model.LinearRegression()
linear.fit(X_train, y_train)
precision = linear.score(X_test, y_test)
print(precision)

with open('suppp.csv', 'w') as csvfile:
    a = linear.predict(td)
    writer = csv.writer(csvfile)
    writer.writerow(a)
    csvfile.close()