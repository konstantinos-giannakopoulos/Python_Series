import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# loading images
colored_image = 'car.jpeg'
#grayscale_image = 'lamborghini-aventador-gray.jpeg'
img = cv.imread(colored_image, cv.IMREAD_COLOR)

# drawing with OpenCV
cv.line(img, (50,50), (250,250), (255,255,0), 15)
cv.rectangle(img, (350,450), (500,350), (0,255,0), 5)
cv.circle(img, (500,200), 100, (255,0,0), 7)
# show the image with OpenCV (RGB)
cv.imshow(colored_image, img)
cv.waitKey(0)
cv.destroyAllWindows()

# drawing with Matplotlib
img = cv.imread(colored_image, cv.IMREAD_COLOR)
x_values = np.linspace(100,900,50)
y_values = np.sin(x_values) * 100 + 300

plt.imshow(img, cmap='gray')
plt.plot(x_values, y_values, 'c', linewidth=5)
plt.show()

# copying elements
img[0:200, 0:300] = [0, 0, 0]
copypart = img[300:500, 300:700]
img[100:300, 100:500] = copypart
img[300:500, 300:700] = [0,0,0]
cv.imshow(colored_image, img)
cv.waitKey(0)
cv.destroyAllWindows()

# saving images and videos
cv.imwrite('car_new.jpeg', img)
# save a video data in a file with OpenCV
capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter('video.avi', fourcc, 60.0, (640,480))
while True:
    ret, frame = capture.read()

    writer.write(frame)

    cv.imshow('Cam', frame)

    if cv.waitKey(1) == ord('x'): #lower FPS => higher delay => less disk space
        break

capture.release()
writer.release()
cv.destroyAllWindows()
