#!/usr/bin/python3

"""
This is the square module
3-square.py
This module contains the Square class
"""


class Square:
    """
class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with
the message size must be an integer
if size is less than 0, raise a ValueError exception with the message
size must be >= 0
Public instance method: def area(self): that returns the current
square area
You are not allowed to import any module
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
