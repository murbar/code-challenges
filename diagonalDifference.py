# https://www.hackerrank.com/challenges/diagonal-difference/problem


def diagonalDifference(arr):
    l_to_r = 0
    r_to_l = 0

    for i, row in enumerate(arr):
        l_to_r += row[i]
        r_to_l += row[::-1][i]

    return abs(l_to_r - r_to_l)


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
desired_result = 15

output = diagonalDifference(arr)
print(output)
print("Passes:", output == desired_result)
