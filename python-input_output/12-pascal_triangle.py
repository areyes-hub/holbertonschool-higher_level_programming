#!/usr/bin/python3
"""
This module contains two functions:
binomial_coeff(a, b) and pascal_triangle(n)
"""


def binomial_coeff(a, b):
    """calculates the binomial coefficient f two numbers"""
    if b > a:
        return 0
    if b == 0 or b == a:
        return 1
    return binomial_coeff(a - 1, b - 1) + binomial_coeff(a - 1, b)


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascals triangle of n
    """
    tri = []
    if n <= 0:
        return tri
    else:
        for r in range(n):
            row = []
            for c in range(r + 1):
                row.append(binomial_coeff(r, c))
            tri.append(row)
    return tri
