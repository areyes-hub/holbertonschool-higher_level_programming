#!/usr/bin/python3
"""
class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """
    Public instance method: def area(self):
    Raises an Exception with the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    """Public instance method that validates value"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
