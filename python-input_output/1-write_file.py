#!/usr/bin/python3
"""
This module contains a function named write_file()
"""


def write_file(filename="", text=""):
    """write_file writes a given text string to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    return len(text)
