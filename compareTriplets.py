# https://www.hackerrank.com/challenges/compare-the-triplets/problem


def compareTriplets(a, b):
    points = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            points[0] += 1
        if a[i] < b[i]:
            points[1] += 1
    return points


a = [5, 6, 7]
b = [3, 6, 10]
desired_result = [1, 1]

output = compareTriplets(a, b)
print(output)
print("Passes:", output == desired_result)
