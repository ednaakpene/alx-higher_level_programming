#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for clm in row:
                print("{:d}".format(clm), end=' ' if clm != row[-1] else '')
            print()
