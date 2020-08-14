import cv2

def nothing(x):
    pass

cv2.namedWindow('result')

color = cv2.imread("pedestrian.jpg")
color = cv2.resize(color,(300,300))
hsv=cv2.cvtColor(color,cv2.COLOR_BGR2HSV)

cv2.createTrackbar('minh', 'result', 0, 180, nothing)
cv2.createTrackbar('mins', 'result', 0, 255, nothing)
cv2.createTrackbar('minv', 'result', 0, 255, nothing)

cv2.createTrackbar('maxh', 'result', 0, 180, nothing)
cv2.createTrackbar('maxs', 'result', 0, 255, nothing)
cv2.createTrackbar('maxv', 'result', 0, 255, nothing)

while(True):
    cv2.imshow("Color", color)
    cv2.imshow("hsv",hsv)            # Раскоментируй, чтобы показать запрет в HSV

    minh = cv2.getTrackbarPos('minh', 'result')
    mins = cv2.getTrackbarPos('mins', 'result')
    minv = cv2.getTrackbarPos('minv', 'result')

    maxh = cv2.getTrackbarPos('maxh', 'result')
    maxs = cv2.getTrackbarPos('maxs', 'result')
    maxv = cv2.getTrackbarPos('maxv', 'result')

    mask = cv2.inRange(hsv, (minh,mins,minv), (maxh,maxs,maxv))
    cv2.imshow('mask', mask)
    #mask = cv2.inRange(hsv, (minb,ming,minr), (maxb,maxg,maxr))    # Раскоментируй, чтобы показать запрет в HSV
    #cv2.imshow('mask', mask)

    result = cv2.bitwise_and(color, color, mask = mask)
    #result = cv2.bitwise_and(hsv, hsv, mask=mask)                  # Раскоментируй, чтобы показать запрет в HSV
    cv2.imshow('result', result)

    if cv2.waitKey(1) == 27:
        break
