#!/usr/bin/python3
'''This py script returns the island perimeter passed to the function'''


def island_perimeter(grid):
    '''Returns the perimeter of the island described in grid.'''
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 sides for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:  # Check top neighbor
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check left neighbor
                    perimeter -= 2

    return perimeter
