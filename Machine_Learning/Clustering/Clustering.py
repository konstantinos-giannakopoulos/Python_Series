import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

# 1) Loading data
digits = load_digits()
data = scale(digits.data)
print(data.shape)

# 2) Training
kmeans = KMeans(n_clusters=10, init='random', n_init=10)
kmeans.fit(data)

#centroids=kmeans.cluster_centers_
#print(centroids)

# 3) Predicting
X_new  = np.array([[0,0,1,1,0,0,0,0,
                   0,0,1,1,0,0,0,0,
                   0,0,1,1,0,0,0,0,
                   0,0,1,1,0,0,0,0,
                   0,0,1,1,0,0,0,0,
                   0,0,1,1,0,0,0,0,
                   0,0,1,1,0,0,0,0,
                   0,0,1,1,0,0,0,0]])
Y_new = kmeans.predict(X_new)
print(Y_new)
