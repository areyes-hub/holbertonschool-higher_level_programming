#!/usr/bin/python3
"""
This module contains a function named from_json_string()
"""
import json
from io import StringIO


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string
    """
    io = StringIO(my_str)
    return json.load(io)
