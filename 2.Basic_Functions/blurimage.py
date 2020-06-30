import cv2

img = cv2.imread('resources/car.jpg')

# Blur the image
blurimg = cv2.GaussianBlur(img, (71,71), 0)

cv2.imshow('image', blurimg)
cv2.waitKey(0)