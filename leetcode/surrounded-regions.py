# https://leetcode.com/problems/surrounded-regions/

'''
input:      2d array 'board' of Xs and Os
output:     modify board in-place with captured regions, O -> X
            regions of connected Os that are surrounded by Xs
            connected if adjacent cells connected horizontally or vertically
            surrounded regions shouldn't be on the border
intuition:  check border cells for Os
            mark all found Os and connected Os to visited
            then iterate over board and capture all Os NOT in visited (change Os to Xs)
complexity: O(n) time and space, where n is number of cells on board
            O(1) space if we drop the visited set and use special char to mark visited
'''

from typing import List


def is_in_bounds(board, row, col):
    return all((row >= 0, row < len(board), col >= 0, col < len(board[0])))


def iterate_adjacent_cells(board, row, col):
    for dR, dC in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        i = row + dR
        j = col + dC
        if is_in_bounds(board, i, j):
            yield (i, j)


def iterate_border_cells(board):
    for row in range(len(board)):
        if row == 0 or row == len(board) - 1:
            # yield all cells in first and last row
            for col in range(len(board[row])):
                yield (row, col)
        else:
            # yield first and last cell in other rows
            yield (row, 0)
            yield (row, len(board[row]) - 1)


def search_connected(board, row, col, target, visited):
    if board[row][col] != target:
        return

    if (row, col) not in visited:
        visited.add((row, col))
        for i, j in iterate_adjacent_cells(board, row, col):
            search_connected(board, i, j, target, visited)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # we could save some space by omitting the visited set and using a
        # special placeholder char to mark visited Os
        # in the final iteration of the board, change visited back to Os
        # and change unvisited Os to Xs

        visited = set()
        for i, j in iterate_border_cells(board):
            search_connected(board, i, j, 'O', visited)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i, j) not in visited:
                    board[i][j] = 'X'


s = Solution()

b1 = [['X', 'X', 'X', 'X'],
      ['X', 'O', 'O', 'X'],
      ['X', 'X', 'O', 'X'],
      ['X', 'O', 'X', 'X']]
s.solve(b1)
assert b1 == [['X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X'],
              ['X', 'O', 'X', 'X']]

b2 = [['O', 'O'],
      ['O', 'O']]
s.solve(b2)
assert b2 == [['O', 'O'],
              ['O', 'O']]

b3 = [['O', 'O', 'O'],
      ['O', 'O', 'O'],
      ['O', 'O', 'O']]
s.solve(b3)
assert b3 == [['O', 'O', 'O'],
              ['O', 'O', 'O'],
              ['O', 'O', 'O']]
