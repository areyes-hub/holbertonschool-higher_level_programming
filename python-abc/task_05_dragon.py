#!/usr/bin/python3
"""
===================
Dragon module
===================
"""


class SwimMixin:
    """class to inherit from"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """class to inherit from"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Inherits from both SwimMixin and FlyMixin classes"""
    def roar(self):
        print("The dragon roars!")
