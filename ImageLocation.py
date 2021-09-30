import cv2 as cv
import numpy as np
import time


def mouse_click(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("{} - {}".format(x, y))
        mouseX, mouseY = x, y

org = cv.imread("ipad/sample29.jpg", cv.IMREAD_UNCHANGED)

cv.imshow("sample", org)
cv.setMouseCallback("sample", mouse_click)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

