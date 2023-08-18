#!/usr/bin/env python3
"""A flask app"""


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def greet():
    message = {"message": "Bienvenue"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
