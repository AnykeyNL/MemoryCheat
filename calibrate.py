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
print ("running in pen mode")
swift.set_mode(3)

print ("releasing motors")
swift.send_cmd_sync('M2019')
time.sleep(1)


input("Place robot correctly")
swift.send_cmd_sync('M2401')
time.sleep(1)

swift.send_cmd_sync('M17')

swift.send_cmd_sync('G0 X200 Y0 Z20 F4000')
time.sleep(2)


print ("get pos")
swift.send_cmd_async('M2231 V0')
print('pos:', swift.send_cmd_sync('P2220'))

swift.flush_cmd(wait_stop=True)
swift.disconnect()