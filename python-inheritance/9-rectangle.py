#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
===========================
module with class Rectangle
===========================
"""


class Rectangle(BaseGeometry):
    """
Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle
description: [Rectangle] <width>/<height>
    """
    def __init__(self, width, height):
        """validate width and height input"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        """Assign the values"""
        self.__width = width
        self.__height = height

    """Calculate the area"""
    def area(self):
        return self.__width * self.__height

    """Implement str method"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
