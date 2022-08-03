import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

'''
Goal: Predict if malignant or benign
'''

# 1) Loading data
data = load_breast_cancer()
print(data.feature_names)
print(data.target_names)

# 2) Preparing data
X = np.array(data.data)
Y = np.array(data.target)

# 3) Splitting data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

# 4) Apply k-NNN, NB, Logistic Regression, Decision Tree, Random Forest
knn = KNeighborsClassifier(n_neighbors=5)
nb = GaussianNB()
lr = LogisticRegression()
dt = DecisionTreeClassifier()
rf = RandomForestClassifier()

knn.fit(X_train, Y_train)
nb.fit(X_train, Y_train)
lr.fit(X_train, Y_train)
dt.fit(X_train, Y_train)
rf.fit(X_train, Y_train)

#accuracy = knn.score(X_test,  Y_test)
print(knn.score(X_test,  Y_test))
print(nb.score(X_test,  Y_test))
print(lr.score(X_test,  Y_test))
print(dt.score(X_test,  Y_test))
print(rf.score(X_test,  Y_test))

# 5) Make predictions
X_new  = np.array([[1.799e+01, 1.038e+01, 1.228e+02, 1.001e+03, 1.184e-01, 2.776e-01, 3.001e-01,
 1.471e-01, 2.419e-01, 7.871e-02, 1.095e+00, 9.053e-01, 8.589e+00, 1.534e+02,
 6.399e-03, 4.904e-02, 5.373e-02, 1.587e-02, 3.003e-02, 6.193e-03, 2.538e+01,
 1.733e+01, 1.846e+02, 2.019e+03, 1.622e-01, 6.656e-01, 7.119e-01, 2.654e-01,
 4.601e-01, 1.189e-01]])
#Y_new = knn.predict(X_new)
print(knn.predict(X_new))
print(nb.predict(X_new))
print(lr.predict(X_new))
print(dt.predict(X_new))
print(rf.predict(X_new))
