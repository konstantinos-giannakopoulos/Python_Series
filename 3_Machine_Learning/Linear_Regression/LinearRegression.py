import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
Goal: Predict G3.
'''

# 1) load data from csv to dataframe
data = pd.read_csv('student/student-mat.csv', sep=';')
print(data.head(3))
#print(data.shape)
#print(data.ndim)
#print(data.size)
#print(data.dtypes)
print()

# 2) Feature selection
data = data[['age', 'sex', 'studytime', 'absences', 'G1', 'G2', 'G3']]
print(data.head(3))
print()

# 3) Convert Categorical to Numerical
data['sex'] = data['sex'].map({'F':0, 'M':1})
print(data.head(3))
print(data.shape)
print()

prediction = 'G3'

# 4) Preparing data
X = np.array(data.drop([prediction],1))
Y = np.array(data[prediction])
print(X.shape)

# 5) Splitting data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

# 6) Apply Linear Regression
model = LinearRegression()
model.fit(X_train, Y_train)
accuracy = model.score(X_test, Y_test)
print(accuracy)

# 7) Make predictions
X_new = np.array([[18, 1, 3, 40, 15, 16]])
Y_new = model.predict(X_new)
print(Y_new)

# 8) Visualizing Correlations
plt.scatter(data['studytime'], data['G3'])
plt.title("Correlation")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

plt.scatter(data['G2'], data['G3'])
plt.title("Correlation")
plt.xlabel("Second Grade")
plt.ylabel("Final Grade")
plt.show()
