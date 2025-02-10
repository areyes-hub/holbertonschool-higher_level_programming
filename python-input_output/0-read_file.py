#!/usr/bin/python3
"""
This module contains a function named read_file()
"""


def read_file(filename=""):
    """read_file reads the contents of a given file"""
    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
