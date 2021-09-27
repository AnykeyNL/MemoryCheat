import cv2 as cv
import numpy as np
import time


def mouse_click(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("{} - {}".format(x, y))
        mouseX, mouseY = x, y




org = cv.imread("ipad/8.PNG", cv.IMREAD_UNCHANGED)
p1 = cv.cvtColor(org, cv.COLOR_BGR2GRAY)

i1 = 10
i2 = 10
i3 = 10

# cv.imshow("org", org)
# cv.imshow("p1", p1)
cv.imshow("p2", p1)
cv.setMouseCallback("p2", mouse_click)

while True:
    ret, p2 = cv.threshold(p1, i1, i2, i3)
    cv.imshow("p2", p2)

    k = cv.waitKey(0)

    if k == ord('q'):
        break

    if k == ord('w'):
        if i1 <= 240:
            i1 = i1 + 10
        print ("{} - {} - {}".format(i1,i2,i3))

    if k == ord('s'):
        if i1 >= 10:
            i1 = i1 - 10
        print("{} - {} - {}".format(i1, i2, i3))

    if k == ord('e'):
        if i2 <= 240:
            i2 = i2 + 10
        print("{} - {} - {}".format(i1, i2, i3))

    if k == ord('d'):
        if i2 >= 10:
            i2 = i2 - 10
        print("{} - {} - {}".format(i1, i2, i3))

    if k == ord('r'):
        if i3 <= 240:
            i3 = i3 + 1
        print("{} - {} - {}".format(i1, i2, i3))

    if k == ord('f'):
        if i3 >= 1:
            i3 = i3 - 1
        print("{} - {} - {}".format(i1, i2, i3))



