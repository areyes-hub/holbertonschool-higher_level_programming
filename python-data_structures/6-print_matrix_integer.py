#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for n in range(len(r)):
            if n == len(r) - 1:
                print("{}".format(r[n]), end="")
            else:
                print("{} ".format(r[n]), end="")
        print()
