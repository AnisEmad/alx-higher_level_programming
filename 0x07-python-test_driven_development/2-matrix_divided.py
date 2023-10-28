#!/usr/bin/python3
""" this matrix_divided module """


def matrix_divided(matrix, div):
    """this function divide a matrix by a number """
    row_lens = []
    for row in matrix:
        row_lens.append(len(row))
        for coulm in row:
            if not (isinstance(coulm, int) or isinstance(coulm, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    comp = row_lens[0]
    for item in row_lens:
        if comp != item:
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list()
    c = 0
    for i in matrix:
        new_list = list()
        for j in i:
            new_list.append(round(j/div, 2))
        new_matrix.append(new_list)
        del new_list
    return new_matrix
