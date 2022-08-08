# filtering

import cv2 as cv
import numpy as np

img = cv.imread('parrot.jpg')
hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

minimum = np.array([100, 60, 0])
maximum = np.array([255, 255, 255])

mask = cv.inRange(hsv, minimum, maximum)
result = cv.bitwise_and(img, img, mask = mask)

# resulting filter mask
cv.imshow('Mask', mask)
cv.waitKey(0)
cv.destroyAllWindows()

# resulting image
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()

# Blurring and Smoothing
averages = np.ones((15,15), np.float32) /225
smoothed = cv.filter2D(result, -1, averages)
cv.imshow('Smoothed', smoothed)
cv.waitKey(0)
cv.destroyAllWindows()

smoothed2 = cv.filter2D(mask, -1, averages)
smoothed2 = cv.bitwise_and(img, img, mask=smoothed2)
cv.imshow('Smoothed2', smoothed2)
cv.waitKey(0)
cv.destroyAllWindows()

# Gaussian and Median Blur
blur = cv.GaussianBlur(result, (15,15), 0)
median = cv.medianBlur(result, 15)
cv.imshow('Median', median)
cv.waitKey(0)
cv.destroyAllWindows()

median2 = cv.medianBlur(mask, 15)
median2 = cv.bitwise_and(img, img, mask=median2)
cv.imshow('Median2', median2)
cv.waitKey(0)
cv.destroyAllWindows()

# filtering camera data
camera = cv.VideoCapture(0)

while True:
    _,img = camera.read()
    
    hsv  = cv.cvtColor(img, cv.COLOR_RBGHSV)
    minimum = np.array([100, 60, 0])
    maximum = np.array([255, 255, 255])
    mask = cv.inRange(hsv, minimum, maximum)

    median = cv.medianBlur(result, 15)
    median = cv.bitwise_and(img, img, mask=median)
    cv.imshow('Median', median)

    if cv.waitKey(5) == ord('x'):
        break
cv.destroyAllWindows()
camera.release()
