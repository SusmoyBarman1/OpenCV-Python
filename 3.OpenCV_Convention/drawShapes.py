import cv2
import numpy as np

img1 = np.zeros((512, 512, 3), np.uint8)

# Draw line: cv2.line(image, (x1, y1), (x2, y2), (B, G, R), thickness)
cv2.line(img1, (0,0), (300, 200), (0, 255, 0), 3)

cv2.imshow('Line 1', img1)

img2 = np.zeros((512, 512, 3), np.uint8)

cv2.line(img2, (0,0), (img2.shape[1], img2.shape[0]), (0, 255, 0), 3)
cv2.imshow('Line 2', img2)


img3 = np.zeros((512, 512, 3), np.uint8)

# Draw rectangle: cv2.rectangle(image, (x1, y1), (x2, y2), (B, G, R), thickness)
cv2.rectangle(img3, (10,10), (150, 150), (100, 110, 120), 3)
cv2.imshow('Rectangle',img3)


cv2.waitKey(0)