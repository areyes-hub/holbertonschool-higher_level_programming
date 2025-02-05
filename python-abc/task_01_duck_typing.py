#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
======================
ABC module
======================
"""


class Shape(ABC):
    """abstract class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Inherits from Shape and implements area and perimeter methods"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * pi

    def perimeter(self):
        if self.radius < 0:
            raise ValueError("radius must be >= 0")
        return self.radius * 2 * pi


class Rectangle(Shape):
    """Inherits from Shape and implements area and perimeter methods"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(obj):
    print("Area: {}\nPerimeter: {}".format(obj.area(), obj.perimeter()))
