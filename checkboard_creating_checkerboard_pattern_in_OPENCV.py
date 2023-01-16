

import cv2
import numpy as np



img = np.zeros((512, 512, 3), np.uint8)

white = True

kkk = 0
kkkk = 0
for i in range(0,4):
    k = 0
    kk = 128
    if(i != 0):
        kkk += 128
    kkkk += 128
    for j in range(0, 4):
        img[kkk:kkkk, k:kk] = (255, 255, 255)
        k = kk + 128
        kk = k + 128

cv2.imshow("img", img)



        


