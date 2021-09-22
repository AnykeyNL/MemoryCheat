import cv2
import numpy



def mouse_click(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("{} - {}".format(x, y))
        mouseX, mouseY = x, y


def AverageColorBox(i, x1,y1, x2, y2):
    r = 0
    g = 0
    b = 0
    p = 0
    xc = x1
    while xc <= x2:
        yc = y1
        while yc <= y2:
            #print ("{} - {}".format(xc,yc))
            r = r + i[yc][xc]
            g = g + i[yc][xc]
            b = b + i[yc][xc]
            p = p + 1
            yc = yc + 1
        xc = xc + 1

    ar = int(r / p)
    ag = int(g / p)
    ab = int(b / p)

    print("Average: ")
    print("r: {}".format(ar))
    print("g: {}".format(ag))
    print("b: {}".format(ab))


    cv2.rectangle(i, (x1,y1),(x2,y2),(0,255,0),2)

    return 0

def DetectGame(imgname):
    img = cv2.imread("TestImages\{}".format(imgname))
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img2, 150, 5, 5)

    height, width = img.shape[:2]
    print ("w: {} h: {}".format(height,width))

    box = 208
    p1 = AverageColorBox(thresh, 719, 475, 719+box, 476+box)
    p2 = AverageColorBox(thresh, 719, 343, 719+box, 343+box)


    cv2.imshow("Test Image", thresh)

    cv2.setMouseCallback("Test Image", mouse_click)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


DetectGame("test_1.jpg")
DetectGame("test_2.jpg")
