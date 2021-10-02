import cv2 as cv
import numpy as np
import msn.Tiles as tiles
#import RobotSequences as robot
import time


def MakeHistory(screen):
    offsetv = 100
    wx1 = 889
    wx2 = wx1 + offsetv
    wy1 = 459
    wy2 = wy1 + offsetv

    win = screen[wx1:wx2, wy1:wy2]
    vis = np.zeros((offsetv, 200), np.float32)
    vis[:offsetv, :offsetv] = win
    vis[:offsetv, offsetv:200] = win


    # Save the image for visualization
    cv.imwrite("winhistory.png", vis)
    cv.imshow("wins", vis)




cap = cv.VideoCapture(1)
ret, frame = cap.read()
MakeHistory(frame)
