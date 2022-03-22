import composites
import logging

from flask import Flask, request
from primitives import RobotController

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.DEBUG)


app = Flask(__name__)
robot_controller = RobotController()


@app.route("/")
def hello_world():
    return "<h1>Hello, World!!</h1>"


@app.route("/demo")
def demo():
    try:
        robot_controller.demo()
        logging.debug("demoed")
        return 200
    except Exception:
        return 400


@app.route("/move", methods=['POST'])
def move():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        robot_controller.move(*args)
        logging.debug(f"Moving to: {*args,}")
        return 200
    except Exception:
        return 400


@app.route("/screw", methods=['POST'])
def screw():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        robot_controller.screw(*args)
        logging.debug(f"Screwing {*args,} degrees")
        return 200
    except Exception:
        return 400


@app.route("/wait", methods=['POST'])
def wait():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        robot_controller.wait(*args)
        logging.debug(f"Waiting {*args,} milliseconds")
        return 200
    except Exception:
        return 400


@app.route("/placePart", methods=['POST'])
def placePart():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        composites.placePart(robot_controller, *args)
        logging.debug(f"Moving part from {args[0:4]} to: {args[4:]}")
        return 200
    except Exception:
        return 400


@app.route("/grip")
def grip():
    try:
        robot_controller.grip()
        return 200
    except Exception:
        return 400


@app.route("/ungrip")
def ungrip():
    try:
        robot_controller.ungrip()
        return 200
    except Exception:
        return 400


@app.route("/clearAlarms")
def clearAlarms():
    try:
        robot_controller.clearAlarms()
        return 200
    except Exception:
        return 400


# TODO: return JSON
@app.route("/getPose")
def getPose():
    pose = robot_controller.getPose()
    return f"{[pose[0], pose[1], pose[2], pose[3]]}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
