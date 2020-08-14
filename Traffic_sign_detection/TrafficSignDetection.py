import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

pedestrian = cv.resize(cv.imread("pedestrian.jpg"), (64, 64))
stop_sign = cv.resize(cv.imread("stopSign.jpg"), (64, 64))
cv.imshow("pedestrian", pedestrian)
cv.imshow("stop_sign",stop_sign)


pedestrian = cv.inRange(pedestrian, (89, 91, 149), (255, 255, 255))
stop_sign = cv.inRange(stop_sign, (89, 91, 149), (255, 255, 255))
cv.imshow("pedestrain_Ch/B", pedestrian)
cv.imshow("stop_sign_Ch/B",stop_sign)

while (True):
    ret,frame= cap.read()
    frame = cv.resize(frame, (300, 200))
    frameBase = frame.copy()
    

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    blur = cv.blur(hsv, (5, 5))
    # cv.imshow("blur", blur)
    thresh = cv.inRange(blur, (0, 138, 153), (25, 255, 255))   # Это пороги для детектирования
    # cv.imshow("thresh", thresh)
    thresh = cv.erode(thresh, None, iterations=1)
    thresh = cv.dilate(thresh, None, iterations=3)
    cv.imshow("mask", thresh)

    countours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # cv.CHAIN_APPROX_SIMPLE
    countours = countours[0]



    if countours:
        countours = sorted(countours, key=cv.contourArea, reverse=True)
        cv.drawContours(frame, countours[0], -1, (255, 0, 255), 3)
        cv.imshow("contour", frame)

        rect = cv.minAreaRect(countours[0])
        box = np.int0(cv.boxPoints(rect))
        cv.drawContours(frame, [box], -1, (0, 255, 0), 3)

        (x, y, w, h) = cv.boundingRect(countours[0])
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), thickness=2, lineType=8, shift=0)
        #cv.imshow("Detect", frame)
        roiImg = frameBase[y:y + h, x:x + w]
        cv.imshow("Detect", roiImg)

        resizedRoi = cv.resize(roiImg, (64, 64))
        cv.imshow("ResizedRoi", resizedRoi)
        sign = cv.inRange(resizedRoi, (89, 91, 149), (255, 255, 255))     # Это пороги для распознавания
        cv.imshow("sign",sign)


        pedestrian_val=0
        stop_sign_val=0

        for i in range(64):
            for j in range(64):
                if (sign[i][j]==pedestrian[i][j]):
                    pedestrian_val+=1
                if (sign[i][j]==stop_sign[i][j]):
                    stop_sign_val+=1

        print (pedestrian_val)
        print (stop_sign_val)

        if pedestrian_val>3100:
            print("pedestrian")
        elif stop_sign_val>2800:
            print("stopSign")
        else:
            print("nothing")

        cv.imshow("frame",frame)

    if cv.waitKey(1) == 27:
        break
