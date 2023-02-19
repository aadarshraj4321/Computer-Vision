
import cv2
import numpy as np



width = 640
height = 400

cap = cv2.VideoCapture("video/4.mp4")


## Create Trackbar

hueLow = 85
hueHigh = 100
satLow = 10
satHigh = 250
valLow = 10
valHigh = 250


def onTrackHueLow(val):
    global hueLow
    hueLow = val
    print("Hue Low : ", hueLow)

def onTrackHueHigh(val):
    global hueHigh
    hueHigh = val
    print("Hue High : ", hueHigh)


def onTrackSatLow(val):
    global satLow
    satLow = val
    print("Sat Low : ", satLow)


def onTrackSatHigh(val):
    global satHigh
    satHigh = val
    print("Sat High : ", satHigh)

def onTrackHueLow(val):
    global hueLow
    hueLow = val
    print("Hue Low : ", hueLow)

def onTrackValLow(val):
    global valLow
    valLow = val
    print("Val Low : ", valLow)

def onTrackValHigh(val):
    global valHigh
    valHigh = val
    print("Val High : ", valHigh)


cv2.namedWindow("objectTracker")
cv2.moveWindow("objectTracker", width, 0)
cv2.createTrackbar("Hue Low", "objectTracker", 10, 179, onTrackHueLow)
cv2.createTrackbar("Hue High", "objectTracker", 20, 179, onTrackHueHigh)
cv2.createTrackbar("Sat Low", "objectTracker", 10, 255, onTrackSatLow)
cv2.createTrackbar("Sat High", "objectTracker",  250, 255, onTrackSatHigh)
cv2.createTrackbar("Value Low", "objectTracker", 10, 255, onTrackValLow)
cv2.createTrackbar("value Hight", "objectTracker", 250, 255, onTrackValHigh)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width, height))
    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])
    mask = cv2.inRange(hsvFrame, lowerBound, upperBound)
    maskInverse = cv2.bitwise_not(mask)
    detectTheObject = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("hsvFrame", hsvFrame)
    cv2.imshow("mask", mask)
    cv2.imshow("detectTheObject", detectTheObject)


    if(cv2.waitKey(1) & 0xff == ord('f')):
        break


cap.release()
cv2.destroyAllWindows()
