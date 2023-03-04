

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





## -------------- Create Pong Game -----------------------------
## Initialize Paddle For Pong Game
paddleWidth = 125
paddleHeight = 25
paddleColor = (255, 255, 255)

## Initialize Ball For Pong Game
ballRadius = 15
ballColor = (0, 0, 255)
ballXPos = int(width / 2)
ballYPos = int(height / 2)
deltaX = 2
deltaY = 2
userScore = 0
remainLive = 5
font = cv2.FONT_HERSHEY_TRIPLEX
## -------------------------------------------------------------




while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))



## ------------- Pong Game ------------------------------------
    cv2.circle(frame, (ballXPos, ballYPos), ballRadius, ballColor, -1)
    cv2.putText(frame, str(userScore), (25, int(6 * paddleHeight)), font, 5, paddleColor, 2)
    cv2.putText(frame, str(remainLive), (width - 125, int(6 * paddleHeight)), font, 5, paddleColor, 2)
##-------------------------------------------------------------






##-------- Hand Detect For Pong Game ---------------------------------
    handData = findHands.Marks(frame)
    for hand in handData:
        cv2.rectangle(frame, (int(hand[8][0] - paddleWidth / 2), 0), (int(hand[8][0] + paddleWidth / 2), paddleHeight), paddleColor, -1)           
##-----------------------------------------------------------







## ------------- Pong Game Logic------------------------------------
    topEdgeBall = ballYPos - ballRadius
    bottomEdgeBall = ballYPos + ballRadius
    leftEdgeBall = ballXPos - ballRadius
    rightEdgeBall = ballXPos + ballRadius

    if(leftEdgeBall <= 0 or rightEdgeBall >= width):
        deltaX = deltaX * (-1)

    if(bottomEdgeBall >= height):
        deltaY = deltaY * (-1)

    if(topEdgeBall <= paddleHeight):
        if(ballXPos >= int(hand[8][0] - paddleWidth / 2) and ballXPos < int(hand[8][0] + paddleWidth / 2)):
            deltaY = deltaY * (-1)
            score += 1
            if(score > 2):
                deltaY *= 2
                deltaX *= 2
        else:
            ballXPos = int(width / 2)
            ballYPos = int(height / 2)
            remainLive -= 1

    ballXPos = ballXPos + deltaX
    ballYPos = ballYPos + deltaY
    if(remainLives == 0):
        break
## ------------------------------------------------------------







##---------------- Show Frame -------------------------------------------

    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
