#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    for ch in my_string:
        if ch == "c" or ch == "C":
            pass
        else:
            new_str.append(ch)
    return "".join(new_str)
