#!/usr/bin/python3
"""
=======================
CountedIterator module
=======================
"""


class CountedIterator:
    """Extends iter method"""
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    """fetches counter value"""
    def get_count(self):
        return self.counter

    """Overrides __next__ method"""
    def __next__(self):
        next(self.iterator)
        self.counter += 1
        return self.counter
