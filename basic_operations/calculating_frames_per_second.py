

import cv2
import time
import numpy as np


cam = cv2.VideoCapture("video/4.mp4")

tLast = time.time()
time.sleep(.1)
fpsFilter = 30
while True:
    time.sleep(0.01)
    dTime = time.time() - tLast
    tLast = time.time()
    ##time.sleep(.001)
    fps = int(1 / dTime)
    fpsFilter = fps * .97 * fps * .03

    ret, frame = cam.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.rectangle(frame, (50, 0), (300, 80), (100, 50, 200), 3)
    cv2.putText(frame, str(fps) + " fps", (50, 50), font, 2, (100, 255, 100), 2)
    ##cv2.putText(frame, str(int(fpsFilter)) + " fps", (50, 50), font, 2, (100, 255, 100), 2)
    
    cv2.imshow("frame", frame)
 
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cam.release()
cv2.destroyAllWindows()
