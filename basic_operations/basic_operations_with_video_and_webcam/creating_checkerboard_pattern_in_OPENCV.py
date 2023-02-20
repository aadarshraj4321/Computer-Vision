

import cv2
import numpy as np



img = np.zeros((512, 512, 3), np.uint8)

white = True


w = 0
ww = True
blackTrue = False
for i in range(0,42):
    kExtra = 0
    k = 42
    for j in range(0, 42):
        if(white):
            img[:k, kExtra:k] = (w, w, w)
            kExtra += 42
            k += 42
            if(w == 0 and ww == True):
                w = 255
                ww = False
            elif(w == 255 and ww == False):
                w = 0
                ww = True

cv2.imshow("img", img)



        


