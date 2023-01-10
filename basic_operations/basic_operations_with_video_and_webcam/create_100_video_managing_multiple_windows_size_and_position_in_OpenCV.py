import cv2
import numpy as np

#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam = cv2.VideoCapture("video/4.mp4")

rows = int(input("Enter number of rows you want : "))
cols = int(input("Enter number of cols you want : "))

width = 640
height = 480

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
ret, frame = cam.read()
##frame = cv2.resize(frame, (width, height))

## Scale the frame with width and height
frame = cv2.resize(frame, (int(width / cols), int(height / cols)))

for row in range(0, rows):
for col in range(0, cols):
windowName = "Window " + str(row) + " x " + str(col)
cv2.imshow(windowName, frame)
cv2.moveWindow(windowName, int(width / cols) * col, int(height / cols + 30) * row)


if(cv2.waitKey(1) & 0xff == ord('f')):
break


cam.release()
cv2.destroyAllWindows()
