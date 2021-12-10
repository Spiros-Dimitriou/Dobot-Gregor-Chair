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
#state = dType.ConnectDobot(api, "", 115200)[0]
#print("Connect status:",CON_STR[state])

#if (state == dType.DobotConnect.DobotConnect_NoError):
    #dType.SetQueuedCmdClear(api)
#Disconnect Dobot
dType.DisconnectDobot(api)
