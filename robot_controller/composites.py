def placePart(primitives, x1, y1, z1, r1, x2, y2, z2, r2):
    primitives.ungrip()
    primitives.move(x1, y1, z1, r1)
    primitives.grip()
    primitives.move(x2, y2, z2, r2)
    primitives.ungrip()


def moveAndScrew(primitives, x, y, z, r, deg):
    primitives.move(x, y, z, r)
    primitives.screw(deg)
