

import cv2
import numpy as np


##-------------------- Detect Hands -----------------------------------------

class MpHands:
    import mediapipe as mp
    def __init__(self, maxHands = 2, tol1 = .5, tol2 = .5):
        self.hands = self.mp.solutions.hands.Hands(False, maxHands, tol1, tol2)

    def Marks(self, frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if(results.multi_hand_landmarks != None):
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks:
                    myHand.append((int(landMark.x * width), int(landMark.y * height)))

                myHands.append(myHand)

        return myHand
                

##--------------------------------------------------------------------

cap = cv2.VideoCapture(0)
width = 600
height = 400

## Class The MyHands Class
findHands = MpHands(2, .5, .5)

## Init For Pong Game
paddleWidth = 125
paddleHeight = 25
paddleColor = (0, 255, 0)


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))


##-------- Hand Detect For Pong Game ---------------------------------
    handData = findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame, (int(hand[8][0] - paddleWidth / 2), 0), (int(hand[8][0] + paddleWidth / 2), paddleHeight), paddleColor, -1)
            
##-----------------------------------------------------------

    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
