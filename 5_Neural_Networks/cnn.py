# Image Classification with a CNN

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


# 1) load and prepare image data
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0
class_names =  ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

for i in range(16):
    plt.subplot(4,4,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i][0]])
    plt.show()

train_images = train_images[:20000]
train_labels = train_labels[:20000]
test_images = test_images[:4000]
test_labels = test_labels[:4000]
    
# 2) building neural network
model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape(32, 32, 3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# 3) training and testing
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images,
          train_labels,
          epochs=10,
          validation_data=(test_images, test_labels))
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

# 4) classifying own images in 32x32 pixel resolution
img1 = cv.imread('car.jpg')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
plt.imshow(im1, cmap=plt.cm.binary)
plt.show()

prediction = model.predict(np.array([img1] / 255))
index = np.argmax(prediction)
print(class_names[index])
