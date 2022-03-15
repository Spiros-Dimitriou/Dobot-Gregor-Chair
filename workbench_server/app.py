from flask import Flask
from flask import request
import composites

app = Flask(__name__)
fixture_status = False


@app.route("/")
def hello_world():
    return "<h1>Hello, World!!</h1>"


@app.route("/fix")
def fix():
    global fixture_status
    fixture_status = True
    return "Fixture fixed"


@app.route("/unfix")
def unfix():
    global fixture_status
    fixture_status = False
    return "Fixture unfixed"


@app.route("/rotateFixture", methods=['POST'])
def rotateFixture():
    body = request.get_json(force=True)
    pos = body["pos"]
    deg = body["deg"]
    return f"Rotated fixture {pos} by {deg} degrees"


@app.route("/rotate")
def rotate():
    return "Workbench rotated"
