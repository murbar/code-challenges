''' https://leetcode.com/problems/word-search/
intuition:      seems like a search problem, DFS, backtracking
                for each letter in board, init a search for the target word
                return early when found
input:          matrix of letters, target word
output:         bool, is target word in the matrix
constraints:    word can be made up of letters in adjacent cells
                (neighboring horizontally or vertically)
                same cell cannot be used more than once
edge cases:     empty matrix
time:           O(n), where n is the number of letters on the board
space:          O(m), call stack could be as large as the length of the target word
'''

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(board, row, col, i, word):
            # have we found our target?
            if i == len(word):
                return True
            # are we outside the bounds of the board?
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            # does current letter match the letter we're looking for?
            if board[row][col] != word[i]:
                return False

            # continue the search
            # set current letter to blank space to mark this location on the board "used"
            current = board[row][col]
            board[row][col] = ' '
            # search all adjacent letters
            found = dfs(board, row+1, col, i+1, word) or \
                dfs(board, row-1, col, i+1, word) or \
                dfs(board, row, col+1, i+1, word) or \
                dfs(board, row, col-1, i+1, word)
            # restore the blank space
            board[row][col] = current
            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(board, row, col, 0, word):
                    return True

        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:
        # can be done with a set tracking the letters that we've visited
        # uses extra space, a set length of the target word
        visited = set()

        def dfs(board, row, col, i, word):
            # have we used this letter already?
            if (row, col) in visited:
                return False
            # have we found our target?
            if i == len(word):
                return True
            # are we outside the bounds of the board?
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            # does current letter match the letter we're looking for?
            if board[row][col] != word[i]:
                return False

            # some checks above could be combined but at the cost of readability

            # mark this letter as "used" for rest of the search
            visited.add((row, col))
            # continue the search with adjacent letters
            found = dfs(board, row+1, col, i+1, word) or \
                dfs(board, row-1, col, i+1, word) or \
                dfs(board, row, col+1, i+1, word) or \
                dfs(board, row, col-1, i+1, word)
            # free up this letter for subsequent searches
            visited.discard((row, col))
            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(board, row, col, 0, word):
                    return True

        return False


s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
assert s.exist(board, 'ABCCED') == True
assert s.exist(board, 'SEE') == True
assert s.exist(board, 'ABCB') == False
assert s.exist2(board, 'ABCCED') == True
assert s.exist2(board, 'SEE') == True
assert s.exist2(board, 'ABCB') == False
