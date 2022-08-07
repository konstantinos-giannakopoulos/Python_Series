import cv2 as cv
import matplotlib.pyplot as plt

# loading images
colored_image = 'car.jpeg'
#grayscale_image = 'lamborghini-aventador-gray.jpeg'
img = cv.imread(colored_image, cv.IMREAD_COLOR)
#img = cv.imread(colored_image, cv.IMREAD_GRAYSCALE)

# show the image with OpenCV (RGB)
cv.imshow(colored_image, img)
cv.waitKey(0)
cv.destroyAllWindows()

# showing images with Matplotlib (BGR)
plt.imshow(img)
plt.show()

# converting color schemes from RGB to BGR
img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imshow(colored_image, img)
cv.waitKey(0)
cv.destroyAllWindows()
# showing images with Matplotlib (proper color)
plt.imshow(img)
plt.show()

# loading videos 1
mp4_video_file = ''
video = cv.VideoCapture(mp4_video_file)
while True:
    ret, frame = video.read()

    if ret:
        cv.imshow('Video', frame)

        if cv.waitKey(30) == ord('x'): #lower FPS => higher delay => less disk space
            break
    else:
        break
    
video.release()
cv.destroyAllWindows()

# loading videos 2
mp4_video_file = ''
while True:
    ret, frame = video.read()

    if ret:
        cv.imshow('Video', frame)

        if cv.waitKey(30) == ord('x'): #lower FPS => higher delay => less disk space
            break
    else:
        video = cv.VideoCapture(mp4_video_file)
    
video.release()
cv.destroyAllWindows()

# loading camera data
video = cv.VideoCapture(0)
while True:
    ret, frame = video.read()

    if ret:
        cv.imshow('Video', frame)

        if cv.waitKey(1) == ord('x'): #lower FPS => higher delay => less disk space
            break
    else:
        video = cv.VideoCapture(0)
    
video.release()
cv.destroyAllWindows()
