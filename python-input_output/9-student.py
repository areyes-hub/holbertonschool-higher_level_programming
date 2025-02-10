#!/usr/bin/python3
"""
Student class module
"""


class Student:
    """
    Defines a Student class with public instance
    attributes: first_name, last_name, age and a
    public instance method: to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
