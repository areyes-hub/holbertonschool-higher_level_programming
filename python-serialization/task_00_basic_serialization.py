#!/usr/bin/python
"""
This module contains the following functions:
serialize_and_save_to_file(),
load_and_deserialize()
"""
import json


def serialize_and_save_to_file(data, filename):
    """serializes and saves data to the specified file"""
    with open(filename, "w", encoding="utf-8") as file:
        encoded = json.dumps(data)
        file.write(encoded)

def load_and_deserialize(filename):
    """loads and deserializes data from the specified file"""
    with open(filename, encoding="utf-8") as file:
        file = file.read()
        return json.loads(file)
