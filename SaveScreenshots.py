import cv2 as cv
import numpy as np
import time

counter = 40
filedir = "ipad/sample{}.jpg"

cap = cv.VideoCapture(0)

while True:

    ret, frame = cap.read()
    cv.imshow("preview",frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if cv.waitKey(1) & 0xFF == ord('s'):
        fname = filedir.format(counter)
        cv.imwrite(fname, frame)
        print ("saved: {}".format(fname))
        counter = counter + 1



