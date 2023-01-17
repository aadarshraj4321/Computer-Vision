
import cv2
import numpy as np



img = np.zeros((512, 512, 3), dtype = np.uint8)


## create line on image
cv2.line(img, (20, 300), (200, 500), (100, 255, 100), 2)

## create rectangle on image
##cv2.rectangle(img, (10, 100), (200, 300), (100, 255, 200), 2)

b = 10
c = 50
d = 20
e = 50
for i in range(0, 10):
    b += 10
    c += 10
    d += 10
    e += 10
    cv2.rectangle(img, (b, d), (c, e), (255, 100, 90), 2)
    




## create circle on image
##cv2.circle(img, (300, 200), 80, (255, 100, 100), 2)
##cv2.circle(img, (300, 200), 70, (255, 100, 100), 2)
    
a = 10
for i in range(0, 10):
    a += 10
    cv2.circle(img, (350, 300), a, (255, 100, 100), 1)

cv2.imshow("img", img)
