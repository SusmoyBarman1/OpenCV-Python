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



# Draw circle: cv2.circle(image, (x,y->center),radius,(color->0,0,0), thickness)
cv2.circle(img3, (400, 50), 30, (255, 255, 0), 5)
cv2.imshow('Rectangle',img3)

#Put text on image: cv2.putText(img3, "Text", (Origin->300, 100), Font, scale, (color-> 0, 150, 0), thickness)
cv2.putText(img3, "OpenCV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)


cv2.imshow('Rectangle',img3)
cv2.waitKey(0)