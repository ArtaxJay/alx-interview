#!/usr/bin/python3
"""
N Queens Problem: Solve the challenge of placing N non-attacking queens
on an N×N chessboard.
"""

import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        # Check vertical attack
        if board[i] == col:
            return False
        # Check diagonal attack
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Use backtracking to find all solutions for the N Queens problem.
    :param n: Size of the board (N x N)
    :param row: Current row being considered
    :param board: List representing the positions of queens
    :param solutions: List to store all solutions
    """
    if row == n:
        # All queens placed; add solution
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1  # Reset the position (backtracking)


def main():
    """Main function to parse input and solve the N Queens problem."""
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

    board = [-1] * n  # Initialize board with -1 (no queens placed)
    solutions = []    # To store solutions
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
