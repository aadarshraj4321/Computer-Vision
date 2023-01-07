import cv2
import numpy as np


width = 320
height = 180

## cv2.CAP_DSHOW ## mean telling windows that we capturing the frame and show the frame direct
##cam = cv2.VideoCapture("video/4.mp4", cv2.CAP_DSHOW)
cam = cv2.VideoCapture(0)

## set the height and width of video or camera
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

## set the frame rate of video or camera video
cam.set(cv2.CAP_PROP_FPS, 5)

## set the video codec 
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ret, frame = cam.read()


    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cam.release()
cv2.destroyAllWindows()
