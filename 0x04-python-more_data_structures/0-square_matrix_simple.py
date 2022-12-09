#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == [] or matrix is None:
    return
    else:
    new_matrix = []
    for column in matrix:
    new_column = list(map(lambda x: x**2, column))
    new_matrix.append(new_column)
    return new_matrix
