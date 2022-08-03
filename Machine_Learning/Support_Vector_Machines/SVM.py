import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

'''
Goal: Predict if malignant or benign
'''

# 1) Loading data
data = load_breast_cancer()
print(data.feature_names)
print(data.target_names)

# 2) Preparing data
X = data.data
Y = data.target

# 3) Splitting data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=30)

# 4) Apply k-NNN, NB, Logistic Regression, Decision Tree, Random Forest
model = SVC(kernel='linear',C=3)
model.fit(X_train, Y_train)
accuracy = model.score(X_test, Y_test)
print(accuracy)

# 5) Make predictions
X_new  = np.array([[1.799e+01, 1.038e+01, 1.228e+02, 1.001e+03, 1.184e-01, 2.776e-01, 3.001e-01,
 1.471e-01, 2.419e-01, 7.871e-02, 1.095e+00, 9.053e-01, 8.589e+00, 1.534e+02,
 6.399e-03, 4.904e-02, 5.373e-02, 1.587e-02, 3.003e-02, 6.193e-03, 2.538e+01,
 1.733e+01, 1.846e+02, 2.019e+03, 1.622e-01, 6.656e-01, 7.119e-01, 2.654e-01,
 4.601e-01, 1.189e-01]])
Y_new = model.predict(X_new)
print(Y_new)
