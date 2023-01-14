import cv2
import numpy as np


##img = np.ones((512, 512, 3), dtype = np.uint8)
##print(img)
##cv2.imshow("img", img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()

frame = np.array([[0, 0, 0], [0, 0, 0],[0, 0, 0]])
print(frame)
#cv2.imshow("frame", frame)
#cv2.waitKey(0)

print("--------------------")
frame2 = np.zeros([100, 100], dtype = np.uint8)
print(frame2)
frame2[10, 20] = 255
frame2[80:100, 80:100] = 255
print(frame2)
cv2.imshow("frame2", frame2)
print("--------------------------")


frame3 = np.zeros([2, 2, 3], dtype = np.uint8)
print(frame3)
frame3[1, 1] = (0, 0, 255)
print(frame3)
cv2.imshow("frame3", frame3)
print("-------------------------------------------------------------------")



frame4 = np.zeros((512, 512, 3), dtype = np.uint8)
frame4[:, 256:] = (0, 0, 255)
print(frame4)
cv2.imshow("frame4", frame4)
print("------------------------------------------------")



frame5 = np.zeros((512, 512, 3), dtype = np.uint8)
frame5[:, :170] = (255, 100, 100)
frame5[:, 171:340] = (50, 100, 100)
frame5[:, 340:512] = (0, 100, 200)
print(frame5)
cv2.imshow("frame5", frame5)
