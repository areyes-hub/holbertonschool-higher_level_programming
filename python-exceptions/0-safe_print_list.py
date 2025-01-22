#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for n in range(0,x):
            print(my_list[n], end="")
            count += 1
        print("")
        return count
    except TypeError:
        print("")
        return count
    except IndexError:
        print("")
        return count
