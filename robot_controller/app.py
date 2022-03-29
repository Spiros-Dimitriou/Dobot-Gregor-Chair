import composites
import logging

from flask import Flask, request, jsonify, make_response
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
        response = jsonify(result="demoed")
        return make_response(response, 200)
    except Exception:
        return


@app.route("/move", methods=['POST'])
def move():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        robot_controller.move(*args)
        logging.debug(f"Moving to: {*args,}")
        response = jsonify(result=f"Moved to: {*args,}")
        return make_response(response, 200)
    except Exception:
        return


@app.route("/screw", methods=['POST'])
def screw():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        robot_controller.screw(*args)
        logging.debug(f"Screwing {*args,} degrees")
        response = jsonify(result=f"Screwed {*args,} degrees")
        return make_response(response, 200)
    except Exception:
        return


@app.route("/wait", methods=['POST'])
def wait():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        robot_controller.wait(*args)
        logging.debug(f"Waiting {*args,} milliseconds")
        response = jsonify(result=f"Waited {*args,} milliseconds")
        return make_response(response, 200)
    except Exception:
        return 400


@app.route("/placePart", methods=['POST'])
def placePart():
    try:
        body = request.get_json(force=True)
        args = list(map(int, body.values()))
        composites.placePart(robot_controller, *args)
        logging.debug(f"Moving part from {args[0:4]} to: {args[4:]}")
        response = jsonify(result=f"Moved part from {args[0:4]} to: {args[4:]}")
        return make_response(response, 200)
    except Exception:
        return
    
    
@app.route("/moveAndScrew", methods=['POST'])
def moveAndScrew():
    try:
        body = request.get_json(force=True)
        logging.debug(f"Body is: {body}")
        args = list(map(int, body.values()))
        composites.moveAndScrew(robot_controller, *args)
        logging.debug(f"Screwing at {args[0:4]} by {args[4:]} degrees")
        response = jsonify(result=f"Screwing at {args[0:4]} by {args[4:]} degrees")
        return make_response(response, 200)
    except Exception:
        return


@app.route("/grip", methods=['POST'])
def grip():
    try:
        robot_controller.grip()
        logging.debug("Gripping")
        response = jsonify(result="gripped")
        return make_response(response, 200)
    except Exception:
        return


@app.route("/ungrip", methods=['POST'])
def ungrip():
    try:
        robot_controller.ungrip()
        logging.debug("Ungripping")
        response = jsonify(result="ungripped")
        return make_response(response, 200)
    except Exception:
        return


@app.route("/clearAlarms", methods=['POST'])
def clearAlarms():
    try:
        robot_controller.clearAlarms()
        logging.debug("Clearing Alarms")
        response = jsonify(result="Cleared Alarms")
        return make_response(response, 200)
    except Exception:
        return


# TODO: return JSON
@app.route("/getPose")
def getPose():
    try:
        pose = robot_controller.getPose()
        logging.debug("Getting pose")
        response = jsonify(result=(pose[0], pose[1], pose[2], pose[3]))
        return make_response(response, 200)
    except Exception:
        return


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
