#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length_of_matrix = len(matrix)
    for i in range(length_of_matrix):
        for j in matrix[i]:
            if j != 0:
                print(" ", end='')
            print("{:d}".format(j),end=" ")
        print()
