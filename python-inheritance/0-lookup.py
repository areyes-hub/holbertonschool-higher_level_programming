#!/usr/bin/python3
"""
A function that returns the list of available
attributes and methods of an object
Prototype: def lookup(obj):
"""


def lookup(obj):
    """
    Returns a list object
    """
    obj_list = [o for o in dir(obj)]
    return obj_list
