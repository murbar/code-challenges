import random

# Use a random pivot to avoid worst-case O(n^2) running time
# when input is in reverse sorted order. Alternatively, use
# the first, last, or middle element.


def less_than(a, b):
    return a - b


def swap(ls, i, j):
    ls[i], ls[j] = ls[j], ls[i]


def partition(ls, comparator, left, right):
    pivot_i = random.randint(left, right)
    pivot = ls[pivot_i]
    while left <= right:
        while ls[left] < pivot:
            left += 1
        while ls[right] > pivot:
            right -= 1

        if comparator(left, right) <= 0:
            swap(ls, left, right)
            left += 1
            right -= 1

    return left


def quicksort(ls, comparator=less_than, left=0, right=None):
    if right is None:
        right = len(ls) - 1

    if left < right:
        pivot = partition(ls, comparator, left, right)
        quicksort(ls, comparator, left, pivot-1)
        quicksort(ls, comparator, pivot, right)

    return ls


if __name__ == '__main__':
    from timer import with_elapsed

    ls1 = [9, 3, 83, 9, 2, 0, 1, 65, 2, 822, 9, 11, 22, 3, 3, 3, 47]
    ls2 = [-6, 9, 0, 1, 17, 91, 0, 178]
    ls3 = [random.randint(0, 1000) for _ in range(1000)]
    ls4 = [random.randint(0, 1000) for _ in range(10000)]
    ls5 = [random.randint(0, 1000) for _ in range(100000)]
    cases = [ls1, ls2, ls3, ls4, ls5]
    for test in cases:

        @with_elapsed
        def do_test():
            return quicksort(test)

        @with_elapsed
        def python_sort():
            return sorted(test)

        native_time, expected = python_sort()
        qs_time, actual = do_test()
        print(
            f"{native_time*1000:0.2f}ms native vs {qs_time*1000:0.2f}ms quicksort - {round(qs_time//native_time)}x slower")
        assert actual == expected
