import cv2 as cv
import numpy as np

# edge detection
img = cv.imread('bookcase.jpg')
edges = cv.Canny(img, 100, 100)
cv.imshow('Edges', edges)
cv.waitKey(0)
cv.destroyAllWindows()

# template matching
img_bgr = cv.imread('laptop.jpg')
img_gray = cv.cvtColor(img_bgr, cv.COLOR_RGB2GRAY)

template = cv.imread('key.jpg')
template_gray = cv.cvtColor(template, cv.COLOR_RGB2GRAY)
#print(template_gray.shape[::-1])
width, height = template_gray.shape[::-1]
result = cv.matchTemplate(img_gray, template_gray, cv.TM_CCOEFF_NORMED)

threshold = 0.8
area = np.where(result >= threshold)

for pixel in zip(*area[::-1]):
    cv.rectangle(img_gray, pixel, (pixel[0] + width, pixel[1] + height), (0, 0, 255), 2)

cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()

# feature matching
img1 = cv.imread('laptop.jpg', 0)
img2 = cv.imread('laptop2.jpg', 0)

orb = cv.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)
matcher = cv.BFMatcher(cv.NORM_HAMMING)#, crossCheck-True)
matches = matcher.match(descriptors1, descriptors2)
matches = sorted(matches, key = lambda x: x.distance)
result = cv.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=2)
result = cv.resize(result, (1600, 900))
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()

# movement detection
video = cv.VideoCapture('people.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(20, 50)
while True:
    _, frame = video.read()
    mask = subtractor.apply(frame)
    cv.imshow('Mask', mask)
    if cv.waitKey(5) == ord('x'):
        break
cv.destroyAllWindows()
video.release()


# object recognition
faces_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv.imread('people.jpg')
img = cv.resize(img, (1400, 900))

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
faces = faces_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,  0, 0), 2)
    cv.putText(img, 'FACE', (x, y+h+30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
cv.imshow('Result', img)
cv.waitKey(0)
cv.destroyAllWindows()
