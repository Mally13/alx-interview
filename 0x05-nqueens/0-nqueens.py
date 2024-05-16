#!/usr/bin/python3
"""A script that solves the nqueens problem"""
import sys


def is_safe(board, row, col, n):
    """Check if there's a queen in the same column or the diagonals"""
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True


def solve_n_queens(board, row, n, solutions):
    """Helper function to handle recursion"""
    if row == n:
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0


def nqueens(n):
    """Solves the nqueens problem"""
    n = int(n)
    if type(n) is int:
        if n < 4:
            print('N must be at least 4')
            exit(1)
        else:
            board = [[0] * n for _ in range(n)]
            lineup = []
            solve_n_queens(board, 0, n, lineup)
            for i, val in enumerate(lineup):
                queens_idx = []
                for j, valin in enumerate(val):
                    for k, valik in enumerate(valin):
                        if valik == 1:
                            queens_idx.append(f"[{j}, {k}]")
                print(queens_idx)

    else:
        print('N must be a number')
        exit(1)



if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: nqueens N')
        exit(1)
    else:
        nqueens(sys.argv[1])
