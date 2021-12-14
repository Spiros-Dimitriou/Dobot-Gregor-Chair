# -*- coding: UTF-8 -*-
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

    """The robotic arm moves from point A to point B"""
    dType.SetEndEffectorSuctionCup(api, 1, 1, isQueued=1)  # Turn on the air pump
    dType.SetPTPCmd(api, 1, 258, -22, -47, 0, isQueued=1)  # Move to point A（258,-22,-47）
    dType.SetPTPCmd(api, 1, 258, -22, 60, 0, isQueued=1)   # Rise from point A
    dType.SetPTPCmd(api, 1, 207, -150, -46, 0, isQueued=1) # Move to point B（207,-150,-46）
    dType.SetWAITCmd(api, 2, isQueued=1)
    dType.SetEndEffectorSuctionCup(api, 1, 0, isQueued=1)  # Turn off the air pump
    dType.SetPTPCmd(api, 1, 207, -150, 60, 0, isQueued=1)  # Rise from point B
    lastIndex = dType.SetPTPCmd(api, 1, 258, -22, 60, 0, isQueued=1)[0]   # Rise from point A

#Disconnect Dobot
dType.DisconnectDobot(api)
