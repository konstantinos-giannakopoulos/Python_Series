from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pandas_datareader import data as web
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

# loading and preparing data
start = dt.datetime(2018,1,1)
end = dt.datetime(2019,1,1)

apple = web.DataReader('AAPL', 'yahoo', start, end)
data = apple['Adj Close']
#print(data.dtype)
#print(data['Adj Close'])

days = 50
apple['Shifted'] = apple['Adj Close'].shift(-days)
apple.dropna(inplace=True)
#print(data.head())

#pd.DataFrame(df)
X = np.array(apple.drop(['Shifted'],1)) # np.array
Y = np.array(apple['Shifted'])
X = preprocessing.scale(X)

# training and testing
X_train, X_test, Y_train, Y_test  = train_test_split(X, Y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
print(accuracy)

# predicting data
X = X[:-days]
X_new = X[-days:]

prediction = clf.predict(X_new)
print(prediction)

