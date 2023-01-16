

import cv2
import numpy as np

boardSize = int(input("Enter the size of boardSize : "))
numSquares = int(input("how many squares in this board : "))
squareSize = int(boardSize / numSquares)



blackColor = (0, 0, 0)
whiteColor = (255, 255, 255)
currentColor = blackColor


boardImg = np.zeros((boardSize, boardSize, 3), dtype = np.uint8)
for row in range(0, numSquares):
    for col in range(0, numSquares):
        boardImg[squareSize * row : squareSize * (row + 1), squareSize * col : squareSize * (col + 1)] = currentColor
        if(currentColor == blackColor):
            currentColor = whiteColor
        else:
            currentColor = blackColor
    if(currentColor == blackColor):
        currentColor = whiteColor
    else:
        currentColor = blackColor

cv2.imshow("boardImg", boardImg)
