import cv2 as cv
import numpy as np
import msn.Tiles as tiles
import RobotSequences as robot
import time

cap = cv.VideoCapture(1)
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

def SaveScreenshot(screenname, round):
    td = time.strftime("%Y%m%d-%H%M%S")
    filename = "results/{}_{}.jpg".format(screenname, td)
    ret, frame = cap.read()
    print ("screenshot saved: {}".format(filename))


    if screenname == "Prize":
        wx = 889
        wy = 459
        winoffset = 107
        winimg = frame[wy:(wy + winoffset), wx:(wx + winoffset) ]

        print ("Saving last win")
        cv.imwrite(filename, frame)
        cv.imwrite("results/lastwin.jpg", frame)
        cv.imwrite("prices/price_{}.jpg".format(round),  winimg)
    else:
        cv.imwrite(filename, frame)
        cv.imwrite("results/last.jpg", frame)

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
    #print ("roboto going to {},{}".format(rx,ry))
    robot.tik(rx, ry)
    #time.sleep(1)
    ret, frame = cap.read()
    largeTile = tiles.GetTile(r, t, 0, frame)
    smallTile = tiles.GetTile(r, t, 1, frame)
    height, width = largeTile.shape[:2]
    #print ("large tile: {} - {}".format(height,width))
    height, width = smallTile.shape[:2]
    #print("small tile: {} - {}".format(height, width))

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
    sl1 = 0
    sl2 = 1.2
    recognize_threshold = 0.98
    totaltiles = tiles.roundinfo[round][6]
    print ("Playing round {} with total tiles: {}".format(gameround, totaltiles))

    tcounter = 0
    #print ("1:tcount {}".format(tcounter))
    # while True:
    #     ret, frame = cap.read()
    #     cv.imshow("ipad",frame)
    #     if cv.waitKey(1) & 0xFF == ord('n'):
    #         break

    while tcounter < totaltiles:
        #print ("tile {}".format(tcounter))
        tile = TouchAndCapture(round, tcounter)
        time.sleep(sl1)
        field.append(tile)
        if tcounter == 0:
            tcounter = tcounter + 1
            # print("2:tcount {}".format(tcounter))
            tile = TouchAndCapture(round, tcounter)
            time.sleep(sl2)
            tcounter = tcounter + 1
            # print("3:tcount {}".format(tcounter))
            field.append(tile)
            #time.sleep(sl1)
        else:
            match = 99
            highest_match = 0
            matchcount = 0
            for check in range(tcounter):  # tile 2-3 bug????????
                r = compare(field[check][0], field[tcounter][1])
                if r > highest_match:
                    highest_match = r
                if r > recognize_threshold:
                    print("1. MATCH SCORE: {} - Matched with tile {}".format(r, check))
                    matchcount = matchcount + 1
                    #print ("found match with file: {}".format(check))
                    if r == highest_match:
                        match = check
                    else:
                        print ("IGNORING MATCH, as a better match was already found!")
                    #break
                #print ("NO Match ")
            if match < 99:
                if matchcount > 1:
                    print("WARNING!!!!!!!!!!! More then one match found....")
                m = TouchAndCapture(round, match)
                time.sleep(sl2)
                tcounter = tcounter + 1
            else:
                print ("1. Nothing found.. Highest match: {}".format(highest_match))
                tcounter = tcounter + 1
                # print("4:tcount {}".format(tcounter))
                tile = TouchAndCapture(round, tcounter)
                # print ("Putting tile {} in memory".format(tcounter))
                field.append(tile)
                time.sleep(sl2)
                match = 99
                highest_match = 0
                matchcount = 0
                for check in range(tcounter - 1):
                    # cv.imshow("c1", field[check][0])
                    # cv.imshow("c2", field[tcounter][0])
                    r = compare(field[check][0], field[tcounter][1])
                    if r > highest_match:
                        highest_match = r
                    if r > recognize_threshold:
                        matchcount = matchcount + 1
                        print("2. MATCH SCORE: {} - Matched with tile {}".format(r, check))
                        if r == highest_match:
                            match = check
                        else:
                            print("IGNORING MATCH, as a better match was already found!")
                    #else:
                        #print("No match found")
                if match < 99:
                    if matchcount > 1:
                        print ("WARNING!!!!!!!!!!! More then one match found....")
                    m = TouchAndCapture(round, tcounter)
                    time.sleep(sl1)
                    m = TouchAndCapture(round, match)
                    time.sleep(sl2)
                else:
                    print("2. Nothing found.. Highest match: {}".format(highest_match))
                tcounter = tcounter + 1

                # print("5:tcount {}".format(tcounter))

    #SaveScreenshot("{}_".format(gameround), gameround)


    # for mcounter in range(totaltiles-1):
    #     for s in range(totaltiles-1):
    #         r = compare(field[mcounter][0], field[s][1])
    #         if r > 0.98:
    #             print ("tile {} matches with tile {}".format(mcounter, s))


    robot.holdpose()














