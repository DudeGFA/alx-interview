#!/usr/bin/python3
"""
        Solves n queens programing problem
        using backtracking algorithm
    """
import sys


def isValid(ROW, COL, board, board_size):
    """
        Checks if a queen can be
        placed on a particular square
    """
    # print("checking...", ROW, COL)
    if 1 not in board[ROW] and 1 not in [board[i][COL]
                                         for i in range(board_size)]:
        diag_col = COL
        diag_row = ROW
        while diag_col > 0 and diag_row > 0:
            diag_col -= 1
            diag_row -= 1
            if board[diag_row][diag_col] == 1:
                return False
        while (ROW > 0) and (COL < board_size - 1):
            COL += 1
            ROW -= 1
            if board[ROW][COL] == 1:
                return False
        return True
    else:
        return False


def findsolution(row, board, board_size):
    """
        Finds possible solution
        to the problem of n queens
    """
    if row >= board_size:
        return
    for col in range(board_size):
        if isValid(row, col, board, board_size):
            board[row][col] = 1
            # print('isValid', row, col)
            findsolution(row + 1, board, board_size)
            if row == board_size - 1:
                soln = [[i, board[i].index(1)] for i in range(len(board))]
                print(soln)
                board[row][board[row].index(1)] = 0
                continue
            if col == board_size - 1 and 1 in board[row - 1]:
                board[row - 1][board[row - 1].index(1)] = 0
        elif col == board_size - 1 and 1 in board[row - 1]:
            # print(board)
            board[row - 1][board[row - 1].index(1)] = 0
            # print(board)


def main():
    """
        main program
    """
    board_size = int(sys.argv[1])
    board = [[0 for i in range(board_size)] for j in range(board_size)]
    findsolution(0, board, board_size)


if __name__ == "__main__":
    main()
