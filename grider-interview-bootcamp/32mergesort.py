# O(n log n)
# usually implemented with two functions and recursion
# sort recursively splits array into two halves until each half contains only one element
# then merge takes over by joining increasingly larger halves until all elements are sorted


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return [*result, *left, *right]


def merge_sort(ls):
    if len(ls) == 1:
        return ls

    midpoint = len(ls) // 2
    left = merge_sort(ls[:midpoint])
    right = merge_sort(ls[midpoint:])
    return merge(left, right)


assert merge([1, 4, 5, 8, 9], [-60, 7, 20]) == [-60, 1, 4, 5, 7, 8, 9, 20]
assert merge([1, 4, 5, 8, 9], []) == [1, 4, 5,  8, 9]
assert merge_sort([10, 0, 97, -30, 5]) == [-30, 0, 5, 10, 97]
assert merge_sort([12, 0]) == [0, 12]
print('All tests passed!')
