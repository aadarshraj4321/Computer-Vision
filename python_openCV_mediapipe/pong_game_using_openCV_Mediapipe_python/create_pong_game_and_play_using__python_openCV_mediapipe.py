

import cv2
import numpy as np
import mediapipe as mp


##-------------------- Detect Hands -----------------------------------------
class MpHands:
    def __init__(self, mode = False, maxHands = 4, detectionCon = .5, modelComplexity = 1, trackCon = .5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplexity = modelComplexity
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    def Marks(self, frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if(results.multi_hand_landmarks != None):
            for handLandMarks in results.multi_hand_landmarks:
                myHand = []
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x * width), int(landMark.y * height)))

                myHands.append(myHand)

        return myHands


    def handConnections(self, frame, draw = True):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frameRGB)

        if(self.results.multi_hand_landmarks):
            for handLms in self.results.multi_hand_landmarks:
                if(draw):
                    self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

        return frame
##--------------------------------------------------------------------





cap = cv2.VideoCapture(0)
width = 600
height = 400



## Class The MyHands Class
findHands = MpHands()





## -------------- Create Pong Game -----------------------------
## Init Paddle For Pong Game
paddleWidth = 140
paddleHeight = 25
paddleColor = (0, 255, 0)

## Init Ball For Pong Game
ballRadius = 13
ballColor = (255, 0, 0)
ballXPos = int(width / 2)
ballYPos = int(height / 2)
deltaX = 5
deltaY = 2
userScore = 0
remainLives = 5
font = cv2.FONT_HERSHEY_DUPLEX
fontTwo = cv2.FONT_HERSHEY_TRIPLEX
## -------------------------------------------------------------




while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width, height))
    frame = cv2.flip(frame, 1)
    findHands.handConnections(frame)
    canny = cv2.Canny(frame, 80, 60)
    



## ------------- Pong Game ------------------------------------
    cv2.circle(frame, (ballXPos, ballYPos), ballRadius, ballColor, -1)
    cv2.putText(frame, "Score : " + str(userScore), (25, int(6 * paddleHeight)), font, 0.8, (0, 0, 255), 1)
    cv2.putText(frame, "Lives : " + str(remainLives), (width - 145, int(6 * paddleHeight)), font, 0.9, (0, 0, 255), 1)
##-------------------------------------------------------------






##-------- Hand Detect For Pong Game ---------------------------------
    handData = findHands.Marks(frame)
    for hand in handData:
        for i in range(0, 21):
            cv2.circle(frame, hand[i], 3, (0, 255, 0), -1)
    for hand in handData:
        cv2.circle(frame, hand[8], 15, (255, 255, 255), 2)
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
            userScore += 1
            remainLives += 1
            if(userScore  == 1 or userScore == 2):
                deltaY *= 2
                deltaX *= 2
        else:
            ballXPos = int(width / 2)
            ballYPos = int(height / 2)
            remainLives -= 1

    ballXPos = ballXPos + deltaX
    ballYPos = ballYPos + deltaY
    if(remainLives == 0):
        break
## ------------------------------------------------------------







##---------------- Show Frame -------------------------------------------

    cv2.imshow("frame", frame)
    cv2.imshow("CannyImage", canny)
    #cv2.imshow("handConnectionsFrame", handConnectionsFrame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
