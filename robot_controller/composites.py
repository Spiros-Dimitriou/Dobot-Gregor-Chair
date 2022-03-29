def placePart(primitives, x1, y1, z1, r1, x2, y2, z2, r2):
    primitives.ungrip()
    primitives.move(x1, y1, z1, r1)
    primitives.grip()
    primitives.move(x2, y2, z2, r2)
    primitives.ungrip()


def moveAndScrew(primitives, x, y, z, r, deg):
    primitives.move(x, y, z, r)
    primitives.doBot.set_end_effector_gripper(True, False)
    primitives.doBot.wait(300)
    primitives.doBot.set_point_to_point_command(1, x, y, z, 150)
    primitives.doBot.set_end_effector_gripper(True, True)
    primitives.doBot.wait(300)
    primitives.doBot.set_point_to_point_command(1, x, y, z, 150 - deg)
    primitives.doBot.set_end_effector_gripper(True, False)
    primitives.doBot.wait(300)
    primitives.doBot.set_end_effector_gripper(False, False)
