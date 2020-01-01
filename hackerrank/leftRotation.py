# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


def rotLeft(a, d):
    return a[d:] + a[:d]


# tests
test_a = [1, 2, 3, 4, 5]
test_d = 4
expected_output = [5, 1, 2, 3, 4]
print('Passes:', rotLeft(test_a, test_d) == expected_output)
