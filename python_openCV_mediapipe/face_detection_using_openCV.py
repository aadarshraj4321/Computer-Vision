
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
width = 640
height = 360


## Face Detection Haarcascade
faceCascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")



while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width, height))

    ## Face Detection Part
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    allFaces = faceCascade.detectMultiScale(grayFrame, 1.3, 5)
    print(allFaces)
    for face in allFaces:
        x, y, w, h = face
        #print("x = ", x, " y = ", y, " w = ", w, " h = ", h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


    cv2.imshow("original Frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
