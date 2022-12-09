#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    return [[i ** 2 for i in j] for j in matrix]
