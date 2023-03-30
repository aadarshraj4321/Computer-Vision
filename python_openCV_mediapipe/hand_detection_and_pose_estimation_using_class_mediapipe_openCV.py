

# import libraries
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

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))


##-------- Hand Detect ---------------------------------
    handData = findHands.Marks(frame)
    for hand in handData:
        for index in [0, 5, 6, 7, 8]:
            cv2.circle(frame, hand[index], 25, (0, 0, 255), 2)

            
##-----------------------------------------------------------

    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()
