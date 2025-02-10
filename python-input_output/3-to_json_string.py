#!/usr/bin/python3
"""
This module contains a function named to_json_string()
"""
import json


def to_json_string(my_obj):
    """returns the json representation of an object"""
    return json.dumps(my_obj)
