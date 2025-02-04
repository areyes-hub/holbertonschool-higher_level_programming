#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module with class Square
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
        super().__init__(size, size)
        self.integer_validator("size", size)
        """Assign the values"""
        self.__size = size

    """Calculate the area"""
    def area(self):
        return self.__size ** 2
