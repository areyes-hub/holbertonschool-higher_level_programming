#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx > len(new_list):
        pass
    else:
        for n in range(len(new_list)):
            if n == idx:
                new_list[n] = element
                break
    return new_list
