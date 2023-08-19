#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    new_matrix = []
    for i in range(length):
        sub_matrix = []
        for j in range(len(matrix[i])):
            new_value = matrix[i][j] ** 2
            sub_matrix.append(new_value)
        new_matrix.append(sub_matrix)
    return new_matrix
