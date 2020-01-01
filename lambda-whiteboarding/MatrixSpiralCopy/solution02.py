# Matrix Spiral Copy

# Given a 2D array(matrix) `inputMatrix` of integers, create a function
# `spiralCopy` that copies `inputMatrix`’s values into a 1D array in a clockwise
# spiral order. Your function then should return that array.

inputMatrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

output = [1, 2, 3, 4, 5, 10, 15, 20, 19,
          18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]


def matrix_spiral_copy(matrix):
    copy = []
    # indexes
    top_row = 0
    right_col = len(matrix[0]) - 1
    bottom_row = len(matrix) - 1
    left_col = 0

    while top_row <= bottom_row and left_col <= right_col:
        # step through to the right
        for col in range(left_col, right_col + 1):
            copy.append(matrix[top_row][col])
        top_row += 1
        # to the bottom
        for row in range(top_row, bottom_row + 1):
            copy.append(matrix[row][right_col])
        right_col -= 1
        # to the left
        if top_row <= bottom_row:
            for col in range(right_col, left_col - 1, -1):
                copy.append(matrix[bottom_row][col])
            bottom_row -= 1
        # back to the top
        if left_col <= right_col:
            for row in range(bottom_row, top_row - 1, -1):
                copy.append(matrix[row][left_col])
            left_col += 1

    return copy


print(matrix_spiral_copy(inputMatrix))
print(output)
