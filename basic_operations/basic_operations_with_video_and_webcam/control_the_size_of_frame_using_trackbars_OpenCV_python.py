
import cv2
import numpy as np



cap = cv2.VideoCapture("video/4.mp4")


## creating trackbars for controling frame size

xAxis = 0
yAxis = 0
def controlFrameCallBackX(val):
    global xAxis
    print("xPos : ", val)
    xAxis = val

def controlFrameCallBackY(val):
    global yAxis
    print("yPos : ", val)
    yAxis = val

cv2.namedWindow("controlFrameSize")
cv2.moveWindow("controlFrameSize", 640, 0)
cv2.resizeWindow("controlFrameSize", 400, 150)
cv2.createTrackbar("xPos", "controlFrameSize", 0, 1272, controlFrameCallBackX)
cv2.createTrackbar("yPos", "controlFrameSize", 0, 560, controlFrameCallBackY)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 400))

    cv2.imshow("frame", frame)
    cv2.moveWindow("frame", xAxis, yAxis)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break


cap.release()
cv2.destroyAllWindows()
