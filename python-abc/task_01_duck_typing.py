#!/usr/bin/python3
"""
======================
ABC module
======================
"""
from abc import ABC, abstractmethod
from math import pi


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
        return abs(self.radius) * 2 * pi


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
