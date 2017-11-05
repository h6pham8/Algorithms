"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""


def set_matrix_zero(matrix):
    zeros = []
    for idx_x, x in enumerate(matrix):
        for idx_y, y in enumerate(x):
            if matrix[idx_x][idx_y] == 0:
                zeros.append([idx_x, idx_y])

    y_length = len(matrix)

    for xy in zeros:
        # x[0] gives the x-axis coordinate
        matrix[xy[0]] = [0] * len(matrix[xy[0]])

        for y in range(0, y_length):
            matrix[y][xy[1]] = 0
