import cv2
import numpy as np

img = cv2.imread('resources/car2.jpg')

# actual size of the image
print(img.shape)

# Resize the image
imgResize = cv2.resize(img, (1000, 800))
print(imgResize.shape)

cv2.imshow('image', img)
cv2.imshow('Resized image', imgResize)
cv2.waitKey(0)