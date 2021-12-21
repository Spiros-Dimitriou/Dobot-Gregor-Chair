# -*- coding: UTF-8 -*-
import sys
import time
import threading
import libs.DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):
    dType.SetPTPCmd(api, 1, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), isQueued=1)[0]

#Disconnect Dobot
dType.DisconnectDobot(api)
