#!/usr/bin/python3

matrix_no = [
    [3, 4, 5, 6],
    [12, 45, 67, 89],
    [1, 2, 7, 9]
]

def print_matrix_integer(matrix=[[]]):
    my_string = ''
    for i in matrix:
        my_string = ', '.join(map(str, i))
        print("{}".format(my_string))
    return my_string