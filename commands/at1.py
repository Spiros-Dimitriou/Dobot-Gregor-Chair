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

    dType.SetQueuedCmdClear(api)
    #open gripper
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    #go to leg base location
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 85, 250, 50, 75, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    #go to workbench
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 200, 160, 30, 42, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    for i in range(2):
        #go to leg location
        dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 255, 25, 10, 9, isQueued = 1)
        dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1)
        dType.SetWAITCmd(api, 0.5, isQueued = 1)
        #return to workbench
        dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 200, 160, 30, 42, isQueued = 1)
        dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
        dType.SetWAITCmd(api, 0.5, isQueued = 1)
        #reorient leg base
        dType.SetPTPCmd(api, 1, 200, 160, 30, 150, isQueued = 1)
        dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1)
        dType.SetWAITCmd(api, 0.5, isQueued = 1)
        dType.SetPTPCmd(api, 1, 200, 160, 30, 150-72, isQueued = 1)
        dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
        dType.SetWAITCmd(api, 0.5, isQueued = 1)
        dType.SetPTPCmd(api, 1, 200, 160, 30, 42, isQueued = 1)

    lastIndex = dType.SetEndEffectorGripper(api, 0, 1, isQueued = 1)[0]
#    dType.SetQueuedCmdStartExec(api)

#    while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
#        dType.dSleep(200)

#    dType.SetQueuedCmdStopExec(api)

#Disconnect Dobot
dType.DisconnectDobot(api)
