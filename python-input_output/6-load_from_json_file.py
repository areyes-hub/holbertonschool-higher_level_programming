#!/usr/bin/python3
"""
This module contains a function named
load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename, encoding="utf-8") as file:
        file = file.read()
        return json.loads(file)
