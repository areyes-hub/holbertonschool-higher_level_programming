#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
Prototype: def is_kind_of_class(obj, a_class):
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is instance of a_class, or is instance of
    a class that inherited from. 
    """
    return isinstance(obj, a_class)
