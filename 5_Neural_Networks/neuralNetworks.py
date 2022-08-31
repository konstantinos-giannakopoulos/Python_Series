# An ordinary Feed Forward Neural Network
# handwritten digit recognition

import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import ssl


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

    
# 1) Loading data
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test)  = mnist.load_data()

X_train = tf.keras.utils.normalize(X_train, axis=1)
X_test = tf.keras.utils.normalize(X_test, axis=1)

# 2) Building the Neural Network
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu)) # 128
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu)) # 128
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 3) Training and Testing
model.fit(X_train, y_train, epochs=3)
loss, accuracy = model.evaluate(X_test, y_test)
print(loss)
print(accuracy)

model.save('digits.model')

# Predicting
model = tf.keras.models.load_model('digits.model')
image = cv.imread('digit_3.png')[:,:,0]
image = np.invert(np.array([image]))
prediction = model.predict(image)
print("Prediction: {}".format(np.argmax(prediction)))
plt.imshow(image[0])
plt.show()
