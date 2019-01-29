# https://www.hackerrank.com/challenges/2d-array/problem


def hourglassSum(arr):
    sums = []
    n_rows, n_cols = len(arr), len(arr[0])
    for row in range(n_rows - 2):
        for col in range(n_cols - 2):
            r1, r2, r3 = arr[row], arr[row+1], arr[row+2]
            c1, c2, c3 = col, col+1, col+2

            values = [r1[c1], r1[c2], r1[c3],
                      r2[c2],
                      r3[c1], r3[c2], r3[c3]]

            sums.append(sum(values))

    return max(sums)


# tests
arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]
expected_output = 19
print("Test 1 passes:", hourglassSum(arr) == expected_output)
