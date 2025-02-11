#!/usr/bin/python3
"""
Pickle module
"""
import pickle


class CustomObject:
    """
    This class implemments serialization
    and deserialization methods for itself
    """

    def __init__(self, name='', age=0, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as file:
            deserial = pickle.load(file)
            return deserial
