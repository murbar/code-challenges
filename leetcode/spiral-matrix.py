# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(n) time/space, n = count of elements in matrix
        spiral = []

        if not matrix:
            return spiral

        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while bottom >= top and right >= left:
            # top, left to right
            for col in range(left, right+1):
                spiral.append(matrix[top][col])
            top += 1
            # right, top to bottom
            # check right
            for row in range(top, bottom+1):
                spiral.append(matrix[row][right])
            right -= 1
            # bottom, right to left
            # check top bound, it has changed since while condition
            if top <= bottom:
                for col in reversed(range(left, right+1)):
                    spiral.append(matrix[bottom][col])
                bottom -= 1
            # left, bottom to top
            # check right bound, it has changed since while condition
            if left <= right:
                for row in reversed(range(top, bottom+1)):
                    spiral.append(matrix[row][left])
                left += 1

        return spiral


s = Solution()
assert s.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert s.spiralOrder([
    [1, 2],
    [4, 5],
    [7, 8]
]) == [1, 2, 5, 8, 7, 4]
assert s.spiralOrder([
    [1, 2]
]) == [1, 2]
assert s.spiralOrder([
    [1, 2, 3, 4]
]) == [1, 2, 3, 4]
assert s.spiralOrder([
    [1],
    [2],
    [3],
    [4]
]) == [1, 2, 3, 4]
assert s.spiralOrder([
    [1]
]) == [1]
assert s.spiralOrder([
    []
]) == []
assert s.spiralOrder([]) == []
assert s.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
assert s.spiralOrder([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]) == [1, 2, 3, 4, 5, 10, 15, 20, 19,
       18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
