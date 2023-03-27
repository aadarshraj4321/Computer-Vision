
## import libraries
import cv2
import  numpy as np



##img = cv2.imread("image/1.jpg")
##img = cv2.resize(img, (640, 400))
##cv2.imshow("img", img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

evt = 0
def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global pnt
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("Mouse Event Was : ", event)
        print("At Pos ", xPos, " ", yPos)
        evt = event
        pnt = (xPos, yPos)

    if(event == cv2.EVENT_LBUTTONUP):
        print("Mouse Event Was : ", event)
        print("At Position ", xPos, " ", yPos)
        evt = event

    if(event == cv2.EVENT_RBUTTONUP):
        print("RightButtonUP : ", event)
        pnt = (xPos, yPos)
        evt = event


cap = cv2.VideoCapture("video/4.mp4")


## listening mouse click
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouseClick)
while True:
    ret, frame = cap.read()

    if(evt == 1 or evt == 4):
        cv2.circle(frame, pnt, 25, (0, 255, 255), 2)
    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()



