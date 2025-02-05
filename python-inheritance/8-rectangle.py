#!/usr/bin/python3
"""
===========================
Module with the Rectangle class
===========================

This module defines a Rectangle class that inherits from BaseGeometry.
It initializes the rectangle with width and height, and validates that
both are positive integers using the integer_validator method from
the BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
