# Make a logo partly transparent and then insert it into an image

import cv2 as cv

img1 = cv.imread('car.jpeg')
img2 = cv.imread('logo.png')
cv.imshow('Logo', img2)
cv.waitKey(0)

#upscale logo
print('Original Dimensions : ',img2.shape)
 
scale_percent = 5000 # percent of original size
width = int(img2.shape[1] * scale_percent / 100)
height = int(img2.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv.resize(img2, dim, interpolation = cv.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv.imshow("Resized image", resized)
cv.waitKey(0)
cv.destroyAllWindows()

img2 = resized


logo_gray = cv.cvtColor(img2, cv.COLOR_RGB2GRAY)
cv.imshow('Logo gray', logo_gray)
cv.waitKey(0)
ret, mask = cv.threshold(logo_gray, 230, 255, cv.THRESH_BINARY_INV)

cv.imshow('Mask', mask)
cv.waitKey(0)
cv.destroyAllWindows()

mask_inv = cv.bitwise_not(mask) # OpenCV
#mask_inv = np.invert(mask) # NumPy
cv.imshow('Mask Inv', mask_inv)
cv.waitKey(0)
cv.destroyAllWindows()

rows, columns, channels = img2.shape
area = img1[0:rows, 0:columns]

img1_bg = cv.bitwise_and(area, area, mask=mask_inv) # define background of the initial picture
img2_fg = cv.bitwise_and(img2, img2, mask=mask) # add the mask with the blue background

result = cv.add(img1_bg, img2_fg) # combine both layers
img1[0:rows, 0:columns] = result

cv.imshow('Result', img1)
cv.waitKey(0)
cv.imwrite('result.jpeg', img1)
cv.destroyAllWindows()

