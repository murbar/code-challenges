# return a n x x spiral matrix
# >>> spiral(3)
# [[1, 2, 3],
#  [8, 9, 4],
#  [7, 6, 5]]


def spiral(n):
    m = [list([0] * n) for _ in range(n)]
    top, left = 0, 0
    bottom, right = n-1, n-1
    i = 1

    while top <= bottom and left <= right:
        # top to the right
        for col in range(left, right+1):
            # print('col', col)
            m[top][col] = i
            i += 1
        top += 1

        # right to the bottom
        for row in range(top, bottom+1):
            m[row][right] = i
            i += 1
        right -= 1

        # bottom to the left
        for col in range(right, left-1, -1):
            m[bottom][col] = i
            i += 1
        bottom -= 1

        # left back to top
        for row in range(bottom, top-1, -1):
            m[row][left] = i
            i += 1
        left += 1

    return m


assert spiral(3) == [[1, 2, 3],
                     [8, 9, 4],
                     [7, 6, 5]]
assert spiral(4) == [[1, 2, 3, 4],
                     [12, 13, 14, 5],
                     [11, 16, 15, 6],
                     [10, 9, 8, 7]]
print('All tests passed!')
