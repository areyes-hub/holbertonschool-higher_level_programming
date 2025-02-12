#!/usr/bin/python3
"""
Student class module
"""


class Student:

    """
    Defines a Student class with public instance
    attributes: first_name, last_name, age and a
    public instance method: to_json(self, attrs=None)
    """

    def __init__(self, first_name="J", last_name="S", age=1):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            new_dict = dict()
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return {
                "last_name": self.last_name,
                "first_name": self.first_name,
                "age": self.age
            }

    def reload_from_json(self, json):
        self.__dict__ = json
