
import cv2
import numpy as np


evt = 0
def mouseClick(event, xPos, yPos, flags, params):
    global pntOne
    global pntTwo
    global evt
    
    if(event == cv2.EVENT_LBUTTONDOWN):
        print(event)
        pntOne = (xPos, yPos)
        evt = event

    if(event == cv2.EVENT_LBUTTONUP):
        print(event)
        pntTwo = (xPos, yPos)
        evt = event


cap = cv2.VideoCapture("video/4.mp4")


cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouseClick)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 400))
    if(evt == 4):
        cv2.rectangle(frame, pntOne, pntTwo, (0, 255, 0), 2)
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    cv2.imshow("frame", frame)
    cv2.imshow("grayFrame", grayFrame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break


cap.release()
cv2.destroyAllWindows()
