import cv2
import numpy as np

img1 = cv2.imread('resources/car2.jpg')
img2 = cv2.imread('resources/card.jpg')

img3 = cv2.resize(img2, (img1.shape[1],img1.shape[0]))

print(img1.shape)
print(img3.shape)


# join horizontaly
imgHor = np.hstack((img1,img3))
'''
# Join vertically
imgVer = np.vstack((img,img))

'''

cv2.imshow('Horizontal join', imgHor)
cv2.waitKey(0)
'''
cv2.imshow('Horizontal join', img3)
cv2.waitKey(0)
'''