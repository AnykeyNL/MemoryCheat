import cv2 as cv
import numpy as np
import time
from matplotlib import pyplot as plt
from skimage.metrics import structural_similarity as compare_ssim


tempnames = ["TestImages/needle_L.jpg", "TestImages/needle_M.jpg", "TestImages/needle_S.jpg", "TestImages/needle_XS.jpg"]
cap = cv.VideoCapture(0)
counter = 0
temps = []
for tempname in tempnames:
    t = cv.imread(tempname, cv.IMREAD_UNCHANGED)
    t = cv.cvtColor(t, cv.COLOR_BGR2GRAY)
    temps.append(cv.Canny(t, 30, 50))

while True:
    #img_rgb = cv.imread("TestImages/test_6.jpg", cv.IMREAD_UNCHANGED)
    ret, img_rgb = cap.read()
    simg = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    simg = cv.Canny(simg, 30, 50)
    cv.imshow("result", img_rgb)
    if cv.waitKey(1) & 0xFF == ord('s'):
        print ("Save screenshot")
        cv.imwrite("TestImages/ipad{}.jpg".format(counter), img_rgb)
        counter = counter + 1

    for t in temps:

        res = cv.matchTemplate(simg, t, cv.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        #print ("{} - {} - {} - {}".format(min_val, max_val, min_loc, max_loc))
        w = t.shape[1]
        h = t.shape[0]
        yloc, xloc = np.where(res >= 0.55)
        print ("{}x{} = {}".format(w,h,len(xloc)))
        if len(xloc) > 0:
            print ("Entering memory mode...")
            cv.imwrite("TestImages/ipad{}.jpg".format(counter), new_img_rgb)
            counter = counter + 1
            for (x,y) in zip(xloc, yloc):
                cv.rectangle(img_rgb, (x,y), (x + w, y + h), (0,255,255), 2)
                cv.imshow("result", img_rgb)

        while len(xloc)>0:
            time.sleep(1)
            ret, new_img_rgb = cap.read()

            index = 0
            for (x, y) in zip(xloc, yloc):
                c1 = cv.matchTemplate(new_img_rgb[y:y+h, x:x+w], img_rgb[y:y+h, x:x+w], cv.TM_CCORR_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
                yloc, xloc = np.where(res >= 0.65)

                print ("change detected: {} - {}".format(index, len(xloc)))
                index = index + 1


            simg = cv.cvtColor(new_img_rgb, cv.COLOR_BGR2GRAY)
            simg = cv.Canny(simg, 30, 50)

            res = cv.matchTemplate(simg, t, cv.TM_CCORR_NORMED)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

            yloc, xloc = np.where(res >= 0.55)





    print (" ")
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    #time.sleep(0.1)

cv.destroyAllWindows()

