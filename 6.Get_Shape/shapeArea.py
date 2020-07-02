import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getContrours(img):

    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # Getting area of the shapes
        area = cv2.contourArea(cnt)
        print(area)
        # Draw Shapes on image
        cv2.drawContours(imgCon, cnt, -1, (255,0,0),3)

        #Get the corner points of the shapes
        perameter = cv2.arcLength(cnt, True)
        points = cv2.approxPolyDP(cnt, 0.02*perameter, True)
        print(len(points))
        objectCorner = len(points)
        x, y, w, h = cv2.boundingRect(points)
        cv2.rectangle(imgCon, (x,y), (x+w, y+h), (0,255,0), 3)

        # Put Text on shapes
        if objectCorner==3: objectType = "Triange"
        elif objectCorner==4: objectType = "Rectangle"
        else: objectType = 'Circle'

        cv2.putText(imgCon, objectType,
                    (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0,0,0), 2)



img = cv2.imread('shapes.png')
imgCanny = cv2.Canny(img, 50,50)

imgCon = img.copy()

getContrours(imgCanny)

# join horizontaly
imgHor = stackImages(0.8,([img,imgCanny,imgCon]))

cv2.imshow('shapes',imgHor)
cv2.waitKey(0)