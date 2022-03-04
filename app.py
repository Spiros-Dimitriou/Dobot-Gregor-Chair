from flask import Flask
from flask import request, jsonify
from primitives import Primitives

app = Flask(__name__)
controller = Primitives()

@app.route("/")
def hello_world():
	return "<h1>Hello, World!</h1>"

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
	
