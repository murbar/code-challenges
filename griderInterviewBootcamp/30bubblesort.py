# O(n^2)


def bubble_sort(ls):
    for i in range(len(ls)):
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]

    return ls


assert bubble_sort([5, 8, 4, 9, 1]) == [1, 4, 5, 8, 9]
assert bubble_sort([10, 0, 97, -30, 5]) == [-30, 0, 5, 10, 97]
print('All tests passed!')
