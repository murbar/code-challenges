# https://leetcode.com/problems/valid-sudoku/

from typing import List


def check(values):
    digits = [d for d in values if d.isnumeric()]
    return len(digits) == len(set(digits))


def rows_valid(board):
    return all(check(row) for row in board)


def cols_valid(board):
    return all(check(row[i] for row in board) for i in range(len(board)))


def squares_valid(board):
    for r in range(0, len(board), 3):
        for c in range(0, len(board), 3):
            if not check(board[r][c:c+3] + board[r+1][c:c+3] + board[r+2][c:c+3]):
                return False

    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return rows_valid(board) and cols_valid(board) and squares_valid(board)


s = Solution()
assert s.isValidSudoku([
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]) == True
assert s.isValidSudoku([
    ['8', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]) == False
