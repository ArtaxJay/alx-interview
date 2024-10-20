#!/usr/bin/python3
"""Backend Interview Challenge: Code Pascal Triangle"""


def pascal_triangle(n):
    """Constructs Pascal Triangle
    based with the rows number equal to n"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # define pascal row and input always position 1
        # in the first and the last positions
        each_row = [0] * (i+1)
        each_row[0] = 1
        each_row[len(each_row) - 1] = 1

        for j in range(1, i):
            # fill in the remaining part of the list
            # aside from the first and the last position
            if j > 0 and j < len(each_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                each_row[j] = a + b

        pascal_triangle[i] = each_row

    return pascal_triangle
