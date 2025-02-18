#!/usr/bin/python3
"""
flask module
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users")
def users():
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def usernames(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    if "name" not in data or "age" not in data or "city" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
