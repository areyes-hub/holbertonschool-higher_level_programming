#!/usr/bin/python3
"""
========================
module with class Square
========================
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square
description: [Square] <width>/<height>
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
