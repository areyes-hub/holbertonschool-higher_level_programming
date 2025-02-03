#!/usr/bin/python3
"""
Function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
specified class ; otherwise False
Prototype: def inherits_from(obj, a_class):
"""
def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    directly or indirectly from a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
