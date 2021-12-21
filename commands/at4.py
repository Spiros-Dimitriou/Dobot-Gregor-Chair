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
    #go to seat conveyor belt and grab a seat
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 130, -260, 35, -30, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    #go to workbench and release the seat
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 230, -180, 60, -35, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    #go to the seat plate location
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 180, -230, 20, -48, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 1, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    #return to workbench
    dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, 230, -180, 60, -35, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    #screw in the seat plate
    dType.SetPTPCmd(api, 1, 230, -180, 60, 0, isQueued = 1)
    dType.SetEndEffectorGripper(api, 1, 0, isQueued = 1)
    dType.SetWAITCmd(api, 0.5, isQueued = 1)
    dType.SetPTPCmd(api, 1, 200, 160, 30, 42, isQueued = 1)

    dType.SetEndEffectorGripper(api, 0, 1, isQueued = 1)

#Disconnect Dobot
dType.DisconnectDobot(api)
