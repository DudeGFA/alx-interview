#!/usr/bin/python3
"""
    Contains function rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
        rotates a 2d matrix
        90 degree clockwise
        in place
    """
    n = len(matrix)
    mid_index = int(n / 2)
    k = 0
    if n % 2 == 0:
        k = 1
    for i in range(n):
        for j in range(i):
            save = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = save

    for i in range(n):
        for j in range(1, mid_index + 1):
            save = matrix[i][mid_index + j - k]
            matrix[i][mid_index + j - k] = matrix[i][mid_index - j]
            matrix[i][mid_index - j] = save
