import cv2

vcap = cv2.VideoCapture(0)

while(1):

    ret, frame = vcap.read()
    if ret == True:
        cv2.imshow('VIDEO', frame)
        key = cv2.waitKey(1)
        if key & 0xFF == 27:
            break

