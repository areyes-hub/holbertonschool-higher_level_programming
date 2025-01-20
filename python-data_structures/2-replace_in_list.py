#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        pass
    else:
        for n in range(len(my_list)):
            if n == idx:
                my_list[n] = element
                break
    return my_list
