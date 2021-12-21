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
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), isQueued=1)[0]
    dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), isQueued=1)[0]
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    dType.SetEndEffectorGripper(api, 0, 0, isQueued = 1)

#Disconnect Dobot
dType.DisconnectDobot(api)
