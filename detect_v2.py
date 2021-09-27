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

i1 = 20
i2 = 210
i3 = 1

ret, p2 = cv.threshold(p1, i1, i2, i3)
p2 = cv.Canny(p2,1, 100, 255 , 7 )
cv.imshow("p2", p2)
cv.setMouseCallback("p2", mouse_click)

simg = p2[502:804, 385:693]
cv.imshow("simg", simg)

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    method = eval(meth)
    res = cv.matchTemplate(simg, p2, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    #print ("{} - {} - {} - {}".format(min_val, max_val, min_loc, max_loc))
    w = simg.shape[1]
    h = simg.shape[0]
    yloc, xloc = np.where(res >= 0.45)
    print ("{}x{} = {}".format(w,h,len(xloc)))
    ximg = org
    if len(xloc) < 20:
        for (x,y) in zip(xloc, yloc):
            print ("{} - {}".format(x,y))
            cv.rectangle(ximg, (x,y), (x + w, y + h), (0,255,255), 2)
        cv.imshow("org", ximg)
        print ("Method: {}".format(method))
        while True:
            k = cv.waitKey(0)
            if k == ord('q'):
                break

while True:
    k = cv.waitKey(0)
    if k == ord('q'):
        break
