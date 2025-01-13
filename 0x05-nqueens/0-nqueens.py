#!/usr/bin/python3
"""
N Queens Problem Solver using Backtracking
"""

import sys


def is_safe(row, col, queens):
    """
    Check if a queen can be safely placed at the given row and column.

    Args:
        row (int): The row to check.
        col (int): The column to check.
        queens(list): D list of already placed queen positions as [row, col]

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for queen_row, queen_col in queens:
        if (
            queen_col == col or
            queen_col + (row - queen_row) == col or
            queen_col - (row - queen_row) == col
        ):
            return False
    return True


def solve_n_queens(n, row=0, queens=None, solutions=None):
    """
    Recursively solve the N Queens problem using backtracking.

    Args:
        n (int): Size of the chessboard and number of queens.
        row (int): Current row being processed.
        queens (list): Positions of already placed queens.
        solutions (list): Collected solutions.

    Returns:
        None
    """
    if queens is None:
        queens = []
    if solutions is None:
        solutions = []

    # Base case: all queens are placed
    if row == n:
        solutions.append(queens[:])
        return

    # Try placing a queen in each column
    for col in range(n):
        if is_safe(row, col, queens):
            queens.append([row, col])
            solve_n_queens(n, row + 1, queens, solutions)
            queens.pop()  # Backtrack

    return solutions


def main():
    """
    Main function to handle input and output for the N Queens solver.
    """
    # Validate input
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solutions = solve_n_queens(n)

    # Print all solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
