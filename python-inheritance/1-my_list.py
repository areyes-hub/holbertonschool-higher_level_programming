#!/usr/bin/python3
"""
class MyList inherits from list
"""


class MyList(list):
    """
Public instance method: def print_sorted(self): that prints the list,
but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
    """
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
