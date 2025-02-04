#!/usr/bin/python3
"""
===================
VerboseList module
===================
"""


class VerboseList(list):
    """Extends list class"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        super().remove(value)

    def pop(self, index = -1):
        print("Popped [{}] from the list.".format(self[index]))
        super().pop(index)
