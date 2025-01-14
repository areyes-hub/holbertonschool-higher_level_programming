#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        char = ord(letter)
        if char > 96 and char < 123:
            char = char - 32
        print(chr(char), end="")
    print("")
