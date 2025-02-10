#!/usr/bin/python3
"""
This module contains a function named append_write()
"""


def append_write(filename="", text=""):
    """append_write appends a given text string to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
