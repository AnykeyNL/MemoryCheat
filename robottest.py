import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
import time

swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})

swift.waiting_ready()
device_info = swift.get_device_info()
print(device_info)

firmware_version = device_info['firmware_version']
if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
    #print ("speed factor)")
    #swift.set_speed_factor(0.0005)
    pass

swift.send_cmd_sync("G0 X270 Y0 Z50 F4000")
time.sleep(2)

# print ("releasing motors")
swift.set_servo_detach()

while True:
    input("place pos1")
    swift.send_cmd_async('M2231 V0')
    print('pos:', swift.send_cmd_sync('P2220'))
