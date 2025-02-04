#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


class Square(Rectangle):
    """
Instantiation with size: def __init__(self, size):
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
    """
    def __init__(self, size):
        """validate size input"""
        self.integer_validator("size", size)

        """Assign the values"""
        self.__size = size

    """Calculate the area"""
    def area(self):
        return self.__size * self.__size
    
    """Implement str method"""
    def __str__(self):
        return f"[{Rectangle.__qualname__}] {self.__size}/{self.__size}"
