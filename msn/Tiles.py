import cv2 as cv
import time

#org = cv.imread("ipad/sample50.jpg", cv.IMREAD_UNCHANGED)
# cap = cv.VideoCapture(0)
# ret, frame = cap.read()
# cv.imshow("test",frame)

# round 0=2 1=4 2=8 3=16 4=32 5=50
roundinfo = []
#                 StartX, StartY, TileSizeL, TileSizeS, Offset, width, total
roundinfo.append([712,310,  92,  72, 42,  2,  2])     #round 0
roundinfo.append([775,385, 155, 120, 60,  2,  4])  #round 1
roundinfo.append([560,385, 155, 120, 60,  4,  8])  #round 2
roundinfo.append([712,310,  92,  72, 42,  4, 16])    #round 3
roundinfo.append([498,335,  82,  65, 38,  8, 32])   #round 4
roundinfo.append([486,320,  80,  60, 16, 10, 50])   #round 5

# def mouse_click(event, x, y, flags, param):
#     global mouseX, mouseY
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         print("{} - {}".format(x, y))
#         mouseX, mouseY = x, y

def GetTile(round, tileid, size, img):
    if size == 0:
        tilesstart = [roundinfo[round][0], roundinfo[round][1]]
        tilessize = roundinfo[round][2]
        tilesoffset = roundinfo[round][4]
    if size==1:
        delta = roundinfo[round][2]-roundinfo[round][3]
        tilesstart = [roundinfo[round][0]+(int(delta/2)), roundinfo[round][1]+(int(delta/2))]
        tilessize = roundinfo[round][3]
        tilesoffset = roundinfo[round][4]+(delta)

    y = int(tileid/roundinfo[round][5])
    x = int(tileid%roundinfo[round][5])

    #print ("Getting tile ({},{}".format(x,y))
    px = tilesstart[0]+(x*tilessize)+(x*tilesoffset)
    py = tilesstart[1]+(y*tilessize)+(y*tilesoffset)
    orgx,orgy = img.shape[:2]
    # print ("Image size {} - {}  - Getting tile ({} - {}) to ({} - {}".format(orgx,orgy, px,py,px + tilessize, py + tilessize))
    # cv.rectangle(frame, (px,py), (px + tilessize, py + tilessize), (0, 255, 255), 2)
    return img[py:py+tilessize, px:px + tilessize]

def demoshow(r):
    # cap = cv.VideoCapture(0)
    # ret, frame = cap.read()

    for t in range(roundinfo[r][6]):
        largeTile = GetTile(r, t, 0, frame)
        smallTile = GetTile(r, t, 1, frame)
        print ("grapped tile: {}".format(t))

    cv.imshow("test", frame)

    while True:
        cv.imshow("test", frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break



# demoshow(5)
