
import cv2
import numpy as np



cap = cv2.VideoCapture("video/4.mp4")


## creating trackbars for controling frame size

xAxis = 0
yAxis = 0
width = 0
height = 0
def controlFrameCallBackX(val):
    global xAxis
    print("xPos : ", val)
    xAxis = val

def controlFrameCallBackY(val):
    global yAxis
    print("yPos : ", val)
    yAxis = val


def controlFrameCallBackWidth(val):
    global width
    print("Width : ", width)
    if(val < 50):
        width = 200
    else:
        width = val


def controlFrameCallBackHeight(val):
    global height
    print("Height : ", height)
    if(val < 125):
        height = 125
    else:
        height = val

cv2.namedWindow("controlFrameSize")
cv2.moveWindow("controlFrameSize", 640, 0)
cv2.resizeWindow("controlFrameSize", 400, 150)
cv2.createTrackbar("xPos", "controlFrameSize", 0, 1272, controlFrameCallBackX)
cv2.createTrackbar("yPos", "controlFrameSize", 0, 560, controlFrameCallBackY)
cv2.createTrackbar("width", "controlFrameSize", 640, 800, controlFrameCallBackWidth)
cv2.createTrackbar("height", "controlFrameSize", 400, 800, controlFrameCallBackHeight)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width, height))

    cv2.imshow("frame", frame)
    cv2.moveWindow("frame", xAxis, yAxis)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break


cap.release()
cv2.destroyAllWindows()
