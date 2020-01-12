# https://leetcode.com/problems/set-matrix-zeroes/

# when encounter a 0, set all values in row and col to 0 except existing zeros
# set to some sentinel value? something non number is fine in Python but what about
# languages with typed arrays?
# if we find a 0, we can set the fist element in its row and col to 0


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # values in array could be any possible number, so we shouldn't use a number as a sentinel
        # with typed languages, this would be more of a problem
        WAS_ZERO = 'zero'

        def mark(val):
            return WAS_ZERO if val == 0 else 0

        for row in range(len(matrix)):
            for value in matrix[row]:
                if value == 0:
                    matrix[row] = [mark(v) for v in matrix[row]]
                    break

        for row in range(len(matrix)):
            for col, value in enumerate(matrix[row]):
                if value == WAS_ZERO:
                    for i in range(len(matrix)):
                        matrix[i][col] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(cols):
                matrix[0][col] = 0

        if is_col:
            for row in range(rows):
                matrix[row][0] = 0

    def setZeroes3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # any 0s in the first row?
        first_row_0 = not all(matrix[0])
        rows = len(matrix)
        cols = len(matrix[0])
        # mark rows and cols that have 0s, start with second row
        for row in range(1, rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        # set marked rows and cols to 0s
        for row in range(1, rows):
            # fill zeros from right to left
            for col in reversed(range(cols)):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        # set first row
        if first_row_0:
            for col in range(cols):
                matrix[0][col] = 0


s = Solution()

m1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
s.setZeroes3(m1)
assert m1 == [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1]
]
m2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
s.setZeroes3(m2)
assert m2 == [
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0]
]
m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
s.setZeroes3(m3)
assert m3 == [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
m4 = [[-1], [2], [3]]
s.setZeroes3(m4)
assert m4 == [[-1], [2], [3]]
