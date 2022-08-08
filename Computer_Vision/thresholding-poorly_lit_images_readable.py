# Make a poorly lit images readable

import cv2 as cv

img = cv.imread('bookpage1.jpeg')
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

ret, threshold = cv.threshold(img_gray, 32, 255, cv.THRESH_BINARY)

gaus = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 4)

cv.imshow('Gaus', gaus)
cv.waitKey(0)
cv.destroyAllWindows()

