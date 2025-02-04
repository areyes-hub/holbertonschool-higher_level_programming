#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
module with class Rectangle
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
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
