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

    #dType.SetQueuedCmdClear(api)
    pose = dType.GetPose(api)[0:3]
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetPTPCmd(api, 1, pose[0], pose[1], pose[2], 150, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    dType.SetPTPCmd(api, 1, pose[0], pose[1], pose[2], 150.0-float(sys.argv[1]), isQueued = 1)
    lastIndex = dType.SetEndEffectorGripper(api, 0, 1, isQueued = 1)[0]
    dType.SetQueuedCmdStartExec(api)

    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
        dType.dSleep(100)

    dType.SetQueuedCmdStopExec(api)

#Disconnect Dobot
dType.DisconnectDobot(api)
