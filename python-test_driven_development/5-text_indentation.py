#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    new_text = text.replace(". ", ".")
    new_text = new_text.replace("? ", "?")
    new_text = new_text.replace(": ", ":")
    while i < len(new_text):
        if new_text[i] in ".?:":
            print(new_text[i], end="\n\n")
            i += 1
        else:
            print(new_text[i], end="")
            i += 1