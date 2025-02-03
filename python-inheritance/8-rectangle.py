#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


class Rectangle(BaseGeometry):
    """
Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
    """
    def __init__(self, width, height):
        """validate width and height input"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        """Assign the values"""
        self.__width = width
        self.__height = height
