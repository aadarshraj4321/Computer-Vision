
import cv2
import numpy as np


cap = cv2.VideoCapture("video/4.mp4")


## Listen the mouse click
evt = 0
xVal = 0
yVal = 0
def colorPickWithMouseCallBack(event, xPos, yPos, flags, params):
    global evt
    global xVal
    global yVal
    if(event == cv2.EVENT_LBUTTONDOWN):
        print(event)
        xVal = xPos
        yVal = yPos
        evt = event
    if(event == cv2.EVENT_RBUTTONUP):
        evt = event
        print(event)
    

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", colorPickWithMouseCallBack)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 400))

    if(evt == 1):
        x = np.zeros((250, 250, 3), dtype = np.uint8)
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color = hsvFrame[yVal][xVal]
        #print(color)
        x[:, :] = color
        cv2.putText(x, str(color), (0, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 1)
        cv2.imshow("ColorPicker", x)
        cv2.moveWindow("ColorPicker", 640 + 100, 0)
        evt = 0
        
    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
