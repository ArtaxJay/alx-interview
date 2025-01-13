#!/usr/bin/python3
'''Solve the N Queens problem using backtracking.'''

import sys

if __name__ == '__main__':
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    # Coordinates of queens placed on the board, e.g., [row, column]
    queens_positions = []
    backtracking = False
    row = 0
    col = 0

    # Iterate through rows of the board
    while row < board_size:
        backtrack = False
        # Iterate through columns in the current row
        while col < board_size:
            # Check if placing a queen in [row, col] is safe
            is_safe = True
            for queen in queens_positions:
                queen_col = queen[1]
                if (
                    queen_col == col or  # Same column
                    queen_col + (row - queen[0]) == col or  # Diagonal \
                    queen_col - (row - queen[0]) == col  # Diagonal /
                ):
                    is_safe = False
                    break

            if not is_safe:
                if col == board_size - 1:
                    backtrack = True
                    break
                col += 1
                continue

            # Place the queen
            queens_positions.append([row, col])

            # If all queens are placed, store the solution and reset
            if row == board_size - 1:
                solutions.append(queens_positions[:])
                for queen in queens_positions:
                    if queen[1] < board_size - 1:
                        row = queen[0]
                        col = queen[1]
                for _ in range(board_size - row):
                    queens_positions.pop()
                if row == board_size - 1 and col == board_size - 1:
                    queens_positions = []
                    backtracking = True
                row -= 1
                col += 1
            else:
                col = 0
            break
        if backtracking:
            break
        # Backtrack to the previous row and try the next column
        if backtrack:
            row -= 1
            while row >= 0:
                col = queens_positions[row][1] + 1
                del queens_positions[row]  # Remove the queen from the board
                if col < board_size:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    # Print all solutions
    for index, solution in enumerate(solutions):
        if index == len(solutions) - 1:
            print(solution, end="")
        else:
            print(solution)
