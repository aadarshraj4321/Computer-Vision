
import cv2
import numpy as np
import mediapipe as mp



cap = cv2.VideoCapture(0)

## Detecting Hands
hands = mp.solutions.hands.Hands(False, 2, .5, .5)
mpDraw = mp.solutions.drawing_utils

while True:
    myHands = []
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    ## Detection Hands
    results = hands.process(frameRGB)
    #print(results)
    if(results.multi_hand_landmarks != None):
        for handLandMarks in result.multi_hand_landmarks:
            myHand = []
            #print(handLandMarks)
            mpDraw.draw_landmarks(frame, handLandMarks, mp.solutions.HAND_CONNECTIONS)
            for Landmark in handLandMarks.landmark:
                #print(Landmark.x, Landmark.y)
                myHand.append((int(Landmark.x * width), int(Landmark.y * height)))
            #print(myHand)
            cv2.circle(frame, myHand[17], 25, (255, 0, 0), 2)
            cv2.circle(frame, myHand[18], 25, (255, 0, 0), 2)
            cv2.circle(frame, myHand[19], 25, (255, 0, 0), 2)
            cv2.circle(frame, myHand[20], 25, (255, 0, 0), 2)
            myHands.append(myHand)
            print(myHands)
            print("-----------------------------------------------")
                

    
    cv2.imshow("frame", frame)
    cv2.imshow("frameRGB", frameRGB)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break


cap.release()
cv2.destroyAllWindows()
