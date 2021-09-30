import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
import time

StartMemory = [ [217.0,-0.99, 1], [322.0, 38.7, 2], [287.1, -32.3, 2], [285.5, 0.4, 4] ]

tiles2 = [ [266, -17], [266, 17] ]
tiles4 = [ [250.5, -17], [250.5, 17],
           [283, -17], [283, 17]]
tiles8 = [ [251.8, -48], [251.8, -17], [251.8, 17], [251.8, 48],
           [281, -48], [281, -17], [281, 17], [281, 48] ]

tiles16 = [ [236.4, -30], [236.4, -9.7], [236.4,12], [236.4,31.4],
            [255.9, -30], [255.9, -9.7], [255.9,12], [255.9,31.4],
            [274.9, -30], [274.9, -9.7], [274.9,12], [274.9,31.4],
            [294.4, -30], [294.4, -9.7], [294.4,12], [294.4,31.4]
            ]

tiles32 = [ [238.2, -65], [238.2, -46], [238.2, -27],[238.2, -9],[238.2, 9],[238.2, 27],[238.2, 46],[238.2, 65],
            [255.13, -65], [255.13, -46], [255.13, -27],[255.13, -9],[255.13, 9],[255.13, 27],[255.13, 46],[255.13, 65],
            [273.23, -65], [273.23, -46], [273.23, -27],[273.23, -9],[273.23, 9],[273.23, 27],[273.23, 46],[273.23, 65],
            [290.42, -65], [290.42, -46], [290.42, -27],[290.42, -9],[290.42, 9],[290.42, 27],[290.42, 46],[290.42, 65],
            ]

tiles50 = [ [236, -65.9], [236, -51.4], [236, -35.8], [236, -21.4], [236, -7.5], [236, 7.5], [236, 21.4], [236, 35.8], [236,51.4], [236,65.9],
            [249.04, -65.9], [249.04, -51.4], [249.04, -35.8], [249.04, -21.4], [249.04, -7.5], [249.04, 7.5], [249.04, 21.4], [249.04, 35.8], [249.04,51.4], [249.04,65.9],
            [263.9, -65.9], [263.9, -51.4], [263.9, -35.8], [263.9, -21.4], [263.9, -7.5], [263.9, 7.5], [263.9, 21.4], [263.9, 35.8], [263.9,51.4], [263.9,65.9],
            [277.8, -65.9], [277.8, -51.4], [277.8, -35.8], [277.8, -21.4], [277.8, -7.5], [277.8, 7.5], [277.8, 21.4], [277.8, 35.8], [277.8,51.4], [277.8,65.9],
            [291.5, -65.9], [291.5, -51.4], [291.5, -35.8], [291.5, -21.4], [291.5, -7.5], [291.5, 7.5], [291.5, 21.4], [291.5, 35.8], [291.5,51.4], [291.5,65.9]
            ]

startgamepos = [ [223.7, -2], [323.5, 38.4], [288.9, -32.4], [285,0] ]

pickprizepos = [ [257.8, -2.7]]

finishgamepos = [ [320.5, 90.8], [216.9, 88.6]]


def tik(x,y):
    z = 23
    tik = 4
    swift.send_cmd_sync("G0 X{} Y{} Z{} F4000".format(x,y,z))
    swift.send_cmd_sync("G0 Z{} F1000".format(z - tik))
    time.sleep(0.3)
    swift.send_cmd_sync("G0 Z{} F2000".format(z))
    #time.sleep(0.5)

def startgame():
    standby()
    for p in startgamepos:
        tik(p[0],p[1])
        time.sleep(2)
    holdpose()

def pickprize():
    standby()
    for p in pickprizepos:
        tik(p[0], p[1])
        time.sleep(2)
    holdpose()

def finishgame():
    standby()
    for p in finishgamepos:
        tik(p[0], p[1])
        time.sleep(5)
    holdpose()

def standby():
    swift.send_cmd_sync("G0 X270 Y0 Z50 F4000")
    time.sleep(2)

def holdpose():
    swift.send_cmd_sync("G0 X124.44 Y0 Z76.6 F4000")
    time.sleep(2)

swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})
swift.waiting_ready()
device_info = swift.get_device_info()
print(device_info)

firmware_version = device_info['firmware_version']
if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
    #print ("speed factor)")
    #swift.set_speed_factor(0.0005)
    pass

#holdpose()
#standby()
#
# # Start Game
# input ("start memory")
# for p in StartMemory:
#     tik(p[0], p[1])
#     time.sleep(p[2])
#
# standby()
#
# #tile2
# for p in tiles2:
#     tik(p[0], p[1])
#     time.sleep(4)
#
# standby()
#
# input ("start 4 tiles")
# for p in tiles4:
#     tik(p[0], p[1])
#     time.sleep(4)
#
# input ("start 8 tiles")
# for p in tiles8:
#     tik(p[0], p[1])
#     time.sleep(4)
#
