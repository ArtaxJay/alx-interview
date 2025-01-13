#!/usr/bin/python3
"""
N Queens Problem Solver
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be safely placed at board[row][col].

    Args:
        board (list): Current board state.
        row (int): Row index.
        col (int): Column index.
        n (int): Size of the board (NxN).

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Solve the N Queens problem using backtracking.

    Args:
        n (int): Size of the board (NxN).
        row (int): Current row index.
        board (list): Current board state.
        solutions (list): Collected solutions.

    Returns:
        None
    """
    if row == n:
        solutions.append([[r, board[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1  # Backtrack


def main():
    """
    Main function to handle input and solve the N Queens problem.
    """
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

    solutions = []
    board = [-1] * n  # Initialize board with -1 (no queens placed)
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
