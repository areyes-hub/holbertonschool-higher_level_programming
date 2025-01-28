#!/usr/bin/python3
"""Defines an empty class Rectangle"""


class Rectangle:
    """
class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with
the message width must be an integer
if width is less than 0, raise a ValueError exception with the message
width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the
message height must be an integer
if height is less than 0, raise a ValueError exception with the message
height must be >= 0
Instantiation with optional width and height:
def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): that returns the rectangle
perimeter:
if width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #
if width or height is equal to 0, return an empty string
repr() should return a string representation of the rectangle to be able
to recreate a new instance by using eval()
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for r in range(self.__height):
                for _ in range(self.__width):
                    print("#", end="")
                if r == self.__height - 1:
                    break
                print("")
            return ""

    def __repr__(self):
        return f"{Rectangle.__name__}({self.__width}, {self.__height})"
