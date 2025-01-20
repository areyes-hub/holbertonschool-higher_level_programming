#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for n in range(len(matrix[r])):
            print("{:d}".format(matrix[r][n]), end="")
            if n != len(matrix[r]) - 1:
                print(" ", end="")
        print("")
