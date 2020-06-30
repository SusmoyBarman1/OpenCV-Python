import cv2

img = cv2.imread('resources/car.jpg')

# Convert RGB image to Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', imgGray)
cv2.waitKey(0)