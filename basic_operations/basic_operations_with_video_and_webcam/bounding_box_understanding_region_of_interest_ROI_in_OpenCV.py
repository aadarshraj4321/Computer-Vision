
import cv2
import numpy as np


cap = cv2.VideoCapture("video/4.mp4")


width = 640
height = 360

snipHeight = 120
snipWidth = 60

boxCenterRow = int(width / 2)
boxCenterColumn = int(height / 2)

deltaMovingRow = 1
deltaMovingCol = 1

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 360))

    frameROI = frame[int(boxCenterRow - snipHeight / 2) : int(boxCenterRow + snipHeight / 2), int(boxCenterColumn - snipWidth / 2) : int(boxCenterColumn + snipWidth / 2)]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame[int(boxCenterRow - snipHeight / 2) : int(boxCenterRow + snipHeight / 2), int(boxCenterColumn - snipWidth / 2) : int(boxCenterColumn + snipWidth / 2)] = frameROI

    if(boxCenterRow - snipHeight / 2 <= 0 or boxCenterRow + snipHeight / 2 >= height):
        deltaMovingRow = deltaMovingRow * (-1)

    if(boxCenterColumn - snipWidth / 2 <= 0 or boxCenterColumn + snipWidth / 2 >= width):
        deltaMovingCol = deltaMovingCol * (-1)

    boxCenterRow = boxCenterRow + deltaMovingRow
    boxCenterColumn = boxCenterColumn + deltaMovingCol

     
    cv2.imshow("frame", frame)
    cv2.imshow("frameROI", frameROI)

    cv2.moveWindow("frame", 0, 0)
    cv2.moveWindow("frameROI", width, 0)

    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
