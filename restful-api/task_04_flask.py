#!/usr/bin/python3
"""
flask module
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


def define_username(dic):
    """
    defines the user's username
    """
    for n, v in dic.items():
        v["username"] = n
        break


user = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}, 
        "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}
define_username(user)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(user)


@app.route("/status")
def status():
    return "OK"


@app.route("/users")
def users():
    names = []
    for u in user:
        names.append(u)
    return names


@app.route("/users/<username>")
def usernames(username):
    if username not in user:
        return '{"error": "User not found"}'
    return user[username]


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not all(key in data for key in ["username", "name", "age", "city"]):
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"]
    if username in user:
        return jsonify({"error": "User already exists"}), 400

    user[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": user[username]}), 201


if __name__ == "__main__":
    app.run()
