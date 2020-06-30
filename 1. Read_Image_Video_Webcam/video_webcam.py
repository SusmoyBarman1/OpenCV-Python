import cv2

'''
# video
cap = cv2.VideoCapture('resources/nature.mp4')

while True:

    success, img = cap.read()

    if not success:
        break
    cv2.imshow('video', img)
    cv2.waitKey(10)

'''
# webcam

cap = cv2.VideoCapture(0)

# define weight, id:3
cap.set(3, 640)
# define height, id:4
cap.set(4, 480)
# define brightness, id:10
cap.set(10, 100)

while True:

    success, img = cap.read()

    if not success:
        break
    cv2.imshow('video', img)
    cv2.waitKey(10)