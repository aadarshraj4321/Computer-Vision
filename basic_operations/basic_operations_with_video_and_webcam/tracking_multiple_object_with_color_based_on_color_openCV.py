
import cv2
import numpy as np


cap = cv2.VideoCapture("video/4.mp4")

## Create Trackbar
highHue = 0
lowHue = 0
lowSat = 0
highSat = 0
lowVal = 0
highVal = 0

def hueHigh(val):
    global highHue
    highHue = val
    print("High Hue : ", highHue)

def hueLow(val):
    global lowHue
    lowHue = val
    print("Low Hue : ", lowHue)

def satLow(val):
    global lowSat
    lowSat = val
    print("Low Sat : ", lowSat)

def satHigh(val):
    global highSat
    highSat = val
    print("High Sat : ", highSat)

def valHigh(val):
    global highVal
    highVal = val
    print("Low Value : ", highVal)

def valLow(val):
    global lowVal
    lowVal = val
    print("High Value : ", lowVal)


cv2.namedWindow("colorObect")
cv2.createTrackbar("Hue High", "colorObect", 10, 179, hueHigh)
cv2.createTrackbar("Hue Low", "colorObect", 20, 179, hueLow)
cv2.createTrackbar("Sat Low", "colorObect", 10, 255, satLow)
cv2.createTrackbar("Sat High", "colorObect", 20, 255, satHigh)
cv2.createTrackbar("Value Low", "colorObect", 10, 255, valLow)
cv2.createTrackbar("Value High", "colorObect",  20, 255, valHigh)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 400))
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    canny = cv2.Canny(frame, 80, 50)

    upperBound = np.array([highSat, highHue, highVal])
    lowerBound = np.array([lowSat, lowHue, lowVal])

    upperBound2 = np.array([200, 100, 255])
    lowerBound2 = np.array([100, 80, 100])
    
    mask = cv2.inRange(hsvFrame, lowerBound, upperBound)
    mask2 = cv2.inRange(hsvFrame, lowerBound2, upperBound2)

    #maskComposite = mask | mask2
    maskComposite = cv2.add(mask, mask2)
    objectDetect = cv2.bitwise_and(frame, frame, mask = mask2)
    

    cv2.imshow("frame", frame)
    cv2.imshow("hsvFrame", hsvFrame)
    cv2.imshow("cannyImage", canny)
    cv2.imshow("objectDetect", objectDetect)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break


cap.release()
cv2.destroyAllWindows()
