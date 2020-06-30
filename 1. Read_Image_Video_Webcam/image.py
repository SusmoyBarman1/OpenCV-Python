import cv2

img = cv2.imread('resources/car.jpg')

cv2.imshow('Car image', img)
cv2.waitKey(0)