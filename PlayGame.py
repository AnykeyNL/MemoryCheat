import PlaySingleRound
import time
import RobotSequences
from glob import glob
from os import stat
import cv2 as cv
import numpy as np

betweenround = 1

for g in range(10):

    countfile = open("counter.txt", "r")
    gamecount = countfile.read()
    gamecount = int(gamecount) + 1
    countfile.close()
    countfile = open("counter.txt", "w")
    countfile.write("{}".format(gamecount))
    countfile.close()

    print ("Game round {}".format(gamecount))

    RobotSequences.startgame()
    time.sleep(3)

    PlaySingleRound.playround(0)
    #time.sleep(betweenround)
    PlaySingleRound.playround(1)
    #time.sleep(betweenround)
    PlaySingleRound.playround(2)
    time.sleep(betweenround)
    PlaySingleRound.playround(3)
    time.sleep(betweenround)
    PlaySingleRound.playround(4)
    time.sleep(betweenround)
    PlaySingleRound.playround(5)
    time.sleep(betweenround)

    RobotSequences.pickprize()
    time.sleep(2)

    PlaySingleRound.SaveScreenshot("Prize", gamecount)

    files = glob("prices/price*.jpg")
    sorted_list = sorted(files, key=lambda x: stat(x).st_mtime, reverse=True)
    truncated_list = sorted_list[-15:]
    wins = []
    for f in truncated_list:
        print(f)
        wins.append(cv.imread(f))
    horimg = np.concatenate(wins, axis=1)
    verimg = np.concatenate(wins, axis=0)
    cv.imwrite("prices/wins_h.jpg", horimg)
    cv.imwrite("prices/wins_v.jpg", verimg)

    time.sleep(2)
    RobotSequences.finishgame()





