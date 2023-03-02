
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
width = 600
height = 400


##---------------------------------------------------------------
## detect hands
hands = mp.solutions.hands.Hands(False, 2, .5, .5)
mpDraw = mp.solutions.drawing_utils

def parseLandMarks(frame):
    myHands = []
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    if(results.multi_hand_landmarks != None):
        for handLandMarks in results.multi_hand_landmarks:
            myHand = []
            for landMark in handLandMarks.landmark:
                myHand.append((int(landMark.x * width), int(landMark.y * height)))

            myHands.append(myHand)

    return myHands
            



##-------------------------------------------------------------

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 400))

    ## ----------------- Detect Hands -----------------------
    myHands = parseLandMarks(frame)
    for hand in MyHands:
        for digit in [4, 8, 12, 16, 20]:
            cv2.circle(frame, hand[digit], 25, (0, 0, 255), 2) 
        #cv2.circle(frame, hand[20], 25, (0, 0, 255), 2)

## ------------------------------------------------------------------

    cv2.imshow("frame", frame)
    if(cv2.waitKey(1) & 0xff == ord('f')):
        break

cap.release()
cv2.destroyAllWindows()








    
