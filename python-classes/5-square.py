#!/usr/bin/python3

"""
This is the square module
5-square.py
This module contains the Square class
"""


class Square:
    """
class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with 
the message size must be an integer
if size is less than 0, raise a ValueError exception with the message 
size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout 
the square with the character #:
if size is equal to 0, print an empty line
    """
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print("")
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print("")
