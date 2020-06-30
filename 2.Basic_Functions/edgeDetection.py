import cv2
import numpy as np

img = cv2.imread('resources/car2.jpg')

kernel = np.ones((5,5), np.uint8)

# Find edges of the image
canny = cv2.Canny(img, 100, 100)

# reduce the number of edges 
lowcanny = cv2.Canny(img, 150, 200)

# increase the thickness of the edges
imgDialation = cv2.dilate(lowcanny, kernel, iterations=1)

# decrease the thickness of the edges
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Dialated image', imgDialation)
cv2.imshow('Canny image', lowcanny)
cv2.imshow('Eroded image', imgEroded)
cv2.imshow('Original image', img)
cv2.waitKey(0)