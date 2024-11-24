"""
This module provides a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix 90 degrees clockwise in-place.

    Parameters:
        matrix (list of list of int): The 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.
    """
    left = 0
    right = len(matrix) - 1

    while left < right:
        for offset in range(right - left):
            top = left
            bottom = right

            # Save the top-left value
            top_left = matrix[top][left + offset]

            # Move bottom-left to top-left
            matrix[top][left + offset] = matrix[bottom - offset][left]

            # Move bottom-right to bottom-left
            matrix[bottom - offset][left] = matrix[bottom][right - offset]

            # Move top-right to bottom-right
            matrix[bottom][right - offset] = matrix[top + offset][right]

            # Move top-left to top-right
            matrix[top + offset][right] = top_left

        left += 1
        right -= 1
