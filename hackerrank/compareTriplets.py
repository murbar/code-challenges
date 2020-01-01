# https://www.hackerrank.com/challenges/compare-the-triplets/problem


def compareTriplets(a, b):
    points = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            points[0] += 1
        if a[i] < b[i]:
            points[1] += 1
    return points


# tests
test_a = [5, 6, 7]
test_b = [3, 6, 10]
expected_output = [1, 1]
print("Passes:", compareTriplets(test_a, test_b) == expected_output)
