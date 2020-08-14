import cv2

def nothing(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow('result')

cv2.createTrackbar('minb', 'result', 0, 255, nothing)
cv2.createTrackbar('ming', 'result', 0, 255, nothing)
cv2.createTrackbar('minr', 'result', 0, 255, nothing)

cv2.createTrackbar('maxb', 'result', 0, 255, nothing)
cv2.createTrackbar('maxg', 'result', 0, 255, nothing)
cv2.createTrackbar('maxr', 'result', 0, 255, nothing)

while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (300,200))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("rgb",frame)
    (H, S, V) = cv2.split(hsv)
    cv2.imshow("hue", H)
    cv2.imshow("saturation", S)
    cv2.imshow("value", V)
    B, G, R = cv2.split(frame)
    cv2.imshow("red", R)
    cv2.imshow("green", G)
    cv2.imshow("blue", B)

    minb = cv2.getTrackbarPos('minb', 'result')
    ming = cv2.getTrackbarPos('ming', 'result')
    minr = cv2.getTrackbarPos('minr', 'result')

    maxb = cv2.getTrackbarPos('maxb', 'result')
    maxg = cv2.getTrackbarPos('maxg', 'result')
    maxr = cv2.getTrackbarPos('maxr', 'result')

    hsv=cv2.blur(hsv,(5,5))
    # cv2.imshow("Blur",hsv)

    mask = cv2.inRange(hsv, (minb,ming,minr), (maxb,maxg,maxr))
    cv2.imshow('mask', mask)

    maskEr=cv2.erode(mask,None,iterations=2)
    # cv2.imshow("Erode",maskEr)

    maskDi = cv2.dilate(maskEr, None, iterations=4)
    # cv2.imshow("Dilate", maskDi)

    result = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow('result', result)

    # result2 = cv2.bitwise_and(color, color, mask=mask)
    # cv2.imshow('result2', result)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
