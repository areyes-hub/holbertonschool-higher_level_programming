#!/usr/bin/python3
"""
This module contains a function named write_file()
"""


def write_file(filename="", text=""):
    """write_file writes a given text string to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    
    with open(filename, "r", encoding="utf-8") as file:
        count = 0
        for words in file.readlines():
            for _ in words:
                count += 1
    return count
