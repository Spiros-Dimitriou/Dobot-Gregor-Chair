import logging

from flask import Flask, jsonify, make_response
from flask import request


logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.DEBUG)

app = Flask(__name__)
fixture_status = False


@app.route("/")
def hello_world():
    return "<h1>Hello, World!!</h1>"


@app.route("/fix", methods=["POST"])
def fix():
    global fixture_status
    fixture_status = True
    logging.debug("Fixing...")
    response = jsonify(result="fixed")
    return make_response(response, 200)


@app.route("/unfix", methods=["POST"])
def unfix():
    global fixture_status
    fixture_status = False
    logging.debug("Unfixing...")
    response = jsonify(result="unfixed")
    return make_response(response, 200)


@app.route("/rotateFixture", methods=["POST"])
def rotateFixture():
    body = request.get_json(force=True)
    args = list(map(int, body.values()))
    logging.debug("Rotating fixture...")
    response = jsonify(result="rotated fixture")
    return make_response(response, 200)


@app.route("/rotate", methods=["POST"])
def rotate():
    logging.debug("Rotating...")
    response = jsonify(result="rotated")
    return make_response(response, 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
