from lib.interface import Interface


class RobotController:
    def __init__(self):
        self.doBot = Interface('/dev/ttyUSB0')
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
        self.doBot.set_point_to_point_command(1, 207, -150, 60, 0)

    def move(self, x, y, z, r):
        self.doBot.set_point_to_point_command(1, x, y, z, r)

    def grip(self):
        self.doBot.set_end_effector_gripper(True, True)
        self.doBot.wait(300)

    def ungrip(self):
        self.doBot.set_end_effector_gripper(True, False)
        self.doBot.wait(300)
        self.doBot.set_end_effector_gripper(False, False)

    def wait(self, ms):
        self.doBot.wait(ms)

    def getPose(self):
        return self.doBot.get_pose()[0:4]

    def clearAlarms(self):
        self.doBot.clear_alarms_state()
