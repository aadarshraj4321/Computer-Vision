
import cv2
import numpy as np



#print(cv2.__version__)
#print(np.__version__)

##cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture("video/4.mp4")


while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (640, 360))
    frame2 = frame.copy()
    frameROI = frame[150 : 210, 250 : 390]
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIBGRGRAY = cv2.cvtColor(frameROIGray, cv2.COLOR_GRAY2BGR)
    #frameROIHSV = cv2.cvtColor(frameROI, cv2.COLOR_BGR2HSV)
    #frame2[150 : 210, 250 : 390] = frameROIHSV
    frame2[150 : 210, 250 : 390] = frameROIBGRGRAY

    cv2.imshow("frame", frame)
    cv2.imshow("frameROI", frameROI)
    cv2.imshow("frameROIGray", frameROIGray)
    #cv2.imshow("frameROIHSV", frameROIHSV)
    cv2.imshow("frameROIBGRGRAY", frameROIBGRGRAY)
    cv2.imshow("frame2", frame2)

    cv2.moveWindow("frame", 650, 0)
    cv2.moveWindow("frameROI", 650 * 2, 0)
    cv2.moveWindow("frameROIGray", 650 * 2, 100)
    #cv2.moveWindow("frameROIHSV", 650 * 2, 200)
    cv2.moveWindow("frameROIBGRGRAY", 650 * 2, 200)
    
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cam.release()
cv2.destroyAllWindows()
