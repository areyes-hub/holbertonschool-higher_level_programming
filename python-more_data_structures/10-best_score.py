#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = ""
    best_value = 0
    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value
    return best_key
