# https://leetcode.com/problems/rotate-image/

# seems similar to the spiral array problem
# 4 pointers, but a little tricky
# rotate teh squares from outside in
# each time incrementing left and top, decrementing right and bottom, until they meet
# works because matrix is always square
# save values that are about to be overwritten, copy values from src to dest
# saved values become source, target values go into saved, and source is copied to target
# only need memory to store values that are about to the overwritten

# another approach involves multiple tranformations of the array
# first transposing on the diagonal, then flipping horizontally

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # linear time where n is the number of elements in the matrix
        # constant space
        if len(matrix) < 2:
            return

        top = 0
        bottom = len(matrix) - 1

        # one "layer" is processed at a time
        while top < bottom:
            # matrix is square, left tracks top, right tracks bottom
            right = bottom
            left = top
            # range is one less than the length of the side of current layer
            # could just as well be right - left
            # iterate of each value in this layer
            for i in range(bottom - top):
                # 4-way swap
                # top left -> top right
                target = matrix[top+i][right]
                matrix[top+i][right] = matrix[top][left+i]
                # prev top right -> bottom right
                source = target
                target = matrix[bottom][right-i]
                matrix[bottom][right-i] = source
                # prev bottom right -> bottom left
                source = target
                target = matrix[bottom-i][left]
                matrix[bottom-i][left] = source
                # prev bottom left -> top left
                matrix[top][left+i] = target
            # move to next inner layer
            top += 1
            bottom -= 1

        # no return

    def rotate2(self, matrix: List[List[int]]) -> None:
        # while this solution is less code, if feel less intuitive to me
        # not sure I would have figured out that rotation == transposition + flip
        # similar performance, O(n) time
        size = len(matrix)
        # transpose
        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip
        for row in matrix:
            for i in range(size // 2):
                # ~ for inverse, handy way to walk from both sides of a list
                # eg. i == 3, ~i == -4, both indexes 4 positions from each side of array
                row[i], row[~i] = row[~i], row[i]

        # no return


s = Solution()
l1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
r1 = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
s.rotate(l1)
assert l1 == r1
l2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
r2 = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]
s.rotate(l2)
assert l2 == r2
l3 = [
    [6, 7],
    [9, 8]
]
r3 = [
    [9, 6],
    [8, 7]
]
s.rotate(l3)
assert l3 == r3
l4 = [[1]]
s.rotate(l4)
assert l4 == [[1]]
l5 = []
s.rotate(l5)
assert l5 == []

l6 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
r6 = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
s.rotate2(l6)
assert l6 == r6
l7 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
r7 = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]
s.rotate(l7)
assert l7 == r7
