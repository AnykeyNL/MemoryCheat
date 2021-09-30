import cv2 as cv
import numpy as np
import msn.Tiles as tiles
import RobotSequences as robot
import time

cap = cv.VideoCapture(0)
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

def SaveScreenshot(screenname):
    td = time.strftime("%Y%m%d-%H%M%S")
    filename = "results/{}_{}.jpg".format(screenname, td)
    ret, frame = cap.read()
    print ("screenshot saved: {}".format(filename))
    cv.imwrite(filename, frame)


def TouchAndCapture(r,t):
    print ("Getting tile {} in round {}".format(t,r))
    if r == 0:
        tiledata = robot.tiles2
    if r == 1:
        tiledata = robot.tiles4
    if r == 2:
        tiledata = robot.tiles8
    if r == 3:
        tiledata = robot.tiles16
    if r == 4:
        tiledata = robot.tiles32
    if r == 5:
        tiledata = robot.tiles50


    rx, ry = tiledata[t]
    print ("roboto going to {},{}".format(rx,ry))
    robot.tik(rx, ry)
    time.sleep(1)
    ret, frame = cap.read()
    largeTile = tiles.GetTile(r, t, 0, frame)
    smallTile = tiles.GetTile(r, t, 1, frame)
    height, width = largeTile.shape[:2]
    print ("large tile: {} - {}".format(height,width))
    height, width = smallTile.shape[:2]
    print("small tile: {} - {}".format(height, width))

    #cv.imshow("capture", largeTile)
    return [largeTile, smallTile]

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

def playround(gameround):
    robot.standby()
    field = []
    round = gameround
    sl1 = 0.2
    sl2 = 0.2
    totaltiles = tiles.roundinfo[round][6]
    print ("total tiles: {}".format(totaltiles))

    tcounter = 0
    print ("1:tcount {}".format(tcounter))
    # while True:
    #     ret, frame = cap.read()
    #     cv.imshow("ipad",frame)
    #     if cv.waitKey(1) & 0xFF == ord('n'):
    #         break

    while tcounter < totaltiles:
        print ("tile {}".format(tcounter))
        tile = TouchAndCapture(round, tcounter)
        field.append(tile)
        if tcounter == 0:
            tcounter = tcounter + 1
            print("2:tcount {}".format(tcounter))
            time.sleep(sl2)
            tile = TouchAndCapture(round, tcounter)
            tcounter = tcounter + 1
            print("3:tcount {}".format(tcounter))
            field.append(tile)
            time.sleep(sl1)
        else:
            match = 99
            for check in range(tcounter-1):
                r = compare(field[check][0], field[tcounter][1])
                if r > 0.98:
                    print ("found match with file: {}".format(check))
                    match = check
                    break
            if match < 99:
                time.sleep(sl2)
                m = TouchAndCapture(round, match)
                tcounter = tcounter + 1
                time.sleep(sl1)
            else:
                tcounter = tcounter + 1
                print("4:tcount {}".format(tcounter))
                time.sleep(sl2)
                tile = TouchAndCapture(round, tcounter)
                print ("Putting tile {} in memory".format(tcounter))
                field.append(tile)
                time.sleep(sl1)
                match = 99
                for check in range(tcounter - 1):
                    # cv.imshow("c1", field[check][0])
                    # cv.imshow("c2", field[tcounter][0])
                    r = compare(field[check][0], field[tcounter][1])

                    if r > 0.95:
                        print("found match with file: {}".format(check))
                        match = check
                if match < 99:
                    time.sleep(sl2)
                    m = TouchAndCapture(round, tcounter)
                    time.sleep(sl2)
                    m = TouchAndCapture(round, match)
                    time.sleep(sl1)
                tcounter = tcounter + 1
                print("5:tcount {}".format(tcounter))


    for mcounter in range(totaltiles-1):
        for s in range(totaltiles-1):
            r = compare(field[mcounter][0], field[s][1])
            if r > 0.98:
                print ("tile {} matches with tile {}".format(mcounter, s))

    robot.holdpose()













