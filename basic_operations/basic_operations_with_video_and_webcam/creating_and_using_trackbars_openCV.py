
import cv2
import numpy as np


cap = cv2.VideoCapture("video/4.mp4")

# Create trackbar
xPos = 0
yPos = 0
radius = 20
thickness = 1
def myCallBackFunctionOne(val):
    global xPos
    print("xPos : ", val)
    xPos = val
    

def myCallBackFunctionTwo(val):
    global yPos
    print("yPos : ", val)
    yPos = val


def myCallBackFunctionThree(val):
    global radius
    print("radius : ", radius)
    radius = val


def myCallBackFunctionFour(val):
    global thickness
    print("Thickness : ", thickness)
    thickness = val
    

width = 640
cv2.namedWindow("newTrackbars")
cv2.resizeWindow("newTrackbars", 400, 150)
cv2.moveWindow("newTrackbars", width , 0)
cv2.createTrackbar("xPos", "newTrackbars", xPos, 640, myCallBackFunctionOne)
cv2.createTrackbar("yPos", "newTrackbars", yPos, 400, myCallBackFunctionTwo)
cv2.createTrackbar("radius", "newTrackbars", radius, 100, myCallBackFunctionThree)
cv2.createTrackbar("thickness", "newTrackbars", thickness, 6, myCallBackFunctionFour)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 400))
    if(thickness == 0):
        thickness = -1
    cv2.circle(frame, (xPos, yPos), radius, (255, 100, 100), thickness)

    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
