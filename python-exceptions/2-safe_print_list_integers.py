#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for n in range(0, x):
            if type(my_list[n]) == int:
                print("{:d}".format(my_list[n]), end="")
                count += 1
        print("")
        return count
    except TypeError:
        print("List index out of range")
