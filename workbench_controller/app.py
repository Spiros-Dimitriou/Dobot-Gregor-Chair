import logging

from flask import Flask
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
    return 200


@app.route("/unfix")
def unfix():
    global fixture_status
    fixture_status = False
    return 200


@app.route("/rotateFixture", methods=['POST'])
def rotateFixture():
    body = request.get_json(force=True)
    pos, deg = body["pos"], body["deg"]
    return 200


@app.route("/rotate")
def rotate():
    return 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
