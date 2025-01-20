#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for n in new_dict:
        new_dict[n] *= 2
    return new_dict
