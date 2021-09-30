import cv2 as cv
import numpy as np
import msn.Tiles as tiles

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

def compare(o1, o2):
    method = eval(methods[3])
    # o1 = cv.cvtColor(o1, cv.COLOR_BGR2GRAY)
    # o2 = cv.cvtColor(o1, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(o1, o2, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    #print ("{} - {} - {} - {}".format(min_val, max_val, min_loc, max_loc))
    #loc, xloc = np.where(res < 0.20)
    #print ("max: {}".format(max_val))
    return max_val

fullimage = cv.imread("ipad/sample45.jpg", cv.IMREAD_UNCHANGED)

round = 3
t1 = tiles.GetTile(round,4,1,fullimage)
#cv.imshow("zoek", t1)

for t in range(tiles.roundinfo[round][6]):
    t2 = tiles.GetTile(round, t,0,fullimage)
    #print ("comparing tile {}:".format(t))
    r = compare(t2,t1)
    if r > 0.98:
        print ("Match tile: {}".format(t))


while True:
    k = cv.waitKey(0)
    if k == ord('q'):
        break


