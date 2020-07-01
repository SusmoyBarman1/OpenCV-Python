import cv2
import numpy as np

img = cv2.imread('resources/card.jpg')

# Basic width and height of a card
width, height = 250, 350

# Corner point of the card
point1 = np.float32([[225, 92], [430, 138], [164, 383], [369, 423]])

# Corner points of cropped image
point2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(point1, point2)

# output image
outputImg = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Actual image', img)
cv2.imshow('Output Image', outputImg)

cv2.waitKey(0)
