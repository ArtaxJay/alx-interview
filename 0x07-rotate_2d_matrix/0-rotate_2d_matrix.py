
#!/usr/bin/python3
'''
This module contains a function that rotates a 2D matrix 90° clockwise
'''


def rotate_2d_matrix(matrix):
    '''
    This function rotates a 2D matrix 90° clockwise
    Returns: Null
    '''
    to_left = 0
    to_right = len(matrix) - 1

    while to_left < to_right:
        for i in range(to_right - to_left):
            to_top, to_bottom = to_left, to_right
            # save topleft  value
            to_top_left = matrix[to_top][to_left + i]
            # move bottom left to top left
            matrix[to_top][to_left + i] =
                matrix[to_bottom - i][to_left]
            # move bottom right to bottom left
            matrix[to_bottom - i][to_left] =
                matrix[to_bottom][to_right - i]
            # move bottom right to bottom left
            matrix[to_bottom][to_right - i] =
            matrix[to_top + i][to_right]
            # move top left to top right
            matrix[to_top + i][to_right] = to_top_left
        to_right -= 1
        to_left += 1
