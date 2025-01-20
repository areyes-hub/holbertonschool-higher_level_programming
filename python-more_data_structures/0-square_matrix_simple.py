#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = [row[:] for row in matrix]
    for r in range(len(matrix_cpy)):
        for n in range(len(matrix_cpy[r])):
            matrix_cpy[r][n] *= matrix_cpy[r][n]
    return matrix_cpy
