#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = [[e ** 2 for e in row] for row in matrix]
    return newm
