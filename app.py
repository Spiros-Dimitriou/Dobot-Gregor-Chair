from flask import Flask
from flask import request  # , jsonify
from primitives import Primitives
import composites

app = Flask(__name__)
controller = Primitives()


@app.route("/")
def hello_world():
    return "<h1>Hello, World!!</h1>"


@app.route("/demo")
def demo():
    controller.demo()
    return "demoed"


@app.route("/move", methods=['POST'])
def move():
    body = request.get_json(force=True)
    x = body["x"]
    y = body["y"]
    z = body["z"]
    r = body["r"]
    controller.move(x, y, z, r)
    return f"Moving to: {x} {y} {z} {r}"


@app.route("/screw", methods=['POST'])
def screw():
    body = request.get_json(force=True)
    deg = body["deg"]
    controller.screw(deg)
    return f"Screwing {deg} degrees"


@app.route("/wait", methods=['POST'])
def wait():
    body = request.get_json(force=True)
    time = body["time"]
    controller.wait(time)
    return f"Waiting {time} milliseconds"


@app.route("/placePart", methods=['POST'])
def placePart():
    body = request.get_json(force=True)
    x1 = body["x1"]
    y1 = body["y1"]
    z1 = body["z1"]
    r1 = body["r1"]
    x2 = body["x2"]
    y2 = body["y2"]
    z2 = body["z2"]
    r2 = body["r2"]
    composites.placePart(controller, x1, y1, z1, r1, x2, y2, z2, r2)
    return f"Moving part from {x1} {y1} {z1} {r1} to: {x2} {y2} {z2} {r2}"


@app.route("/grip")
def grip():
    controller.grip()
    return "gripped"


@app.route("/ungrip")
def ungrip():
    controller.ungrip()
    return "ungriped"


@app.route("/clearAlarms")
def clearAlarms():
    controller.clearAlarms()
    return "Alarms cleared"


@app.route("/getPose")
def getPose():
    pose = controller.getPose()
    return f"{[pose[0], pose[1], pose[2], pose[3]]}"
