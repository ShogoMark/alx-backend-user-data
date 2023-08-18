#!/usr/bin/env python3
"""A flask app"""

from auth import Auth
from flask import Flask, request, jsonify

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=['GET'])
def greet():
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=["POST"])
def users():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            return jsonify({"message": "Missing email or password"}), 400

        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
