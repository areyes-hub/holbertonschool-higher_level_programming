#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
====================
ABC module
====================
"""


class Animal(ABC):
    """Abstract class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Inherits from class Animal and implements sound method"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Inherits from class Animal and implements sound method"""
    def sound(self):
        return "Meow"
