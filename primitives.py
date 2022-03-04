import time
import threading
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
from lib.interface import Interface

class Primitives:
	def __init__(self):
		self.doBot = Interface('/dev/ttyUSB1')
		if self.doBot.connected():
			print(f'doBot: {self.doBot} is connected.')
		else:
			print(f'doBot: {self.doBot} is not connected. Terminating demoCommand.py...')

	def demo(self):
		self.doBot.set_end_effector_gripper(True, True)
		self.doBot.set_point_to_point_command(1, 258, -22, 0, 0)
		self.doBot.set_point_to_point_command(1, 258, -22, 60, 0)
		self.doBot.set_point_to_point_command(1, 207, -150, 0, 0)
		self.doBot.set_end_effector_gripper(True, False)
		self.doBot.wait(500)
		self.doBot.set_end_effector_gripper(False, False)
		self.doBot.set_point_to_point_command( 1, 207, -150, 60, 0)
		
	def move(self, x, y, z, r):
		self.doBot.set_point_to_point_command(1, x, y, z, r)
		
	def screw(self, deg):
		self.doBot.set_end_effector_gripper(True, False)
		self.doBot.wait(300)
		pose = self.doBot.get_pose()[0:3]
		self.doBot.set_point_to_point_command(1, pose[0], pose[1], pose[2], 150)
		self.doBot.set_end_effector_gripper(True, True)
		self.doBot.wait(300)
		self.doBot.set_point_to_point_command(1, pose[0], pose[1], pose[2], 150-deg)
		self.doBot.set_end_effector_gripper(True, False)
		self.doBot.wait(300)
		self.doBot.set_end_effector_gripper(False, False)

