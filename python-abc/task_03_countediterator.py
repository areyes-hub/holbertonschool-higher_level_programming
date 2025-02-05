#!/usr/bin/python3
"""
=======================
CountedIterator module
=======================
"""


class CountedIterator(object):
    """Extends iter cass"""
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        if not next(self.iterator):
            raise StopIteration
        return self.counter
