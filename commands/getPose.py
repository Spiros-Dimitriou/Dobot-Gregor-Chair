# -*- coding: UTF-8 -*-
import sys
import time
import threading
import libs.DobotDllType as dType
import json

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

#Load Dll
api = dType.load()

#Connect Dobot
state = dType.ConnectDobot(api, "", 115200)[0]
#print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):

    pose = dType.GetPose(api)[0:4]
    pose = {'x':str(pose[0]), 'y':str(pose[1]), 'z':str(pose[2]), 'r':str(pose[3])}
    print(pose)

#Disconnect Dobot
dType.DisconnectDobot(api)
