from glob import glob
from os import stat
import cv2 as cv
import numpy as np

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

