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
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            new_dict = dict()
            for i in range(len(attrs)):
                if attrs[i] not in self.__dict__:
                    continue
                new_dict[attrs[i]] = self.__dict__[attrs[i]]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__ = json
