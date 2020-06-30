import cv2
import numpy as np


img = cv2.imread('resources/car2.jpg')

# Cropping the image
imgCropped = img[:200, 200:500]

cv2.imshow('image', img)
cv2.imshow('Cropped image', imgCropped)
cv2.waitKey(0)