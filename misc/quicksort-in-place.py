import random

# Use a random pivot to avoid worst-case O(n^2) running time
# when input is in reverse sorted order. Alternatively, use
# the first, last, or middle element.


def swap(ls, i, j):
    ls[i], ls[j] = ls[j], ls[i]


def partition(ls, low, high):
    pivot_i = random.randint(low, high)
    swap(ls, low, pivot_i)

    pivot = ls[low]
    i = j = low + 1
    while j <= high:
        if ls[j] <= pivot:
            swap(ls, i, j)
            i += 1
        j += 1

    swap(ls, low, i-1)
    return i - 1


def quicksort(ls, low=0, high=None):
    if high is None:
        high = len(ls) - 1

    if low < high:
        pivot = partition(ls, low, high)
        quicksort(ls, low, pivot-1)
        quicksort(ls, pivot+1, high)

    return ls


if __name__ == '__main__':
    ls1 = [9, 3, 83, 9, 2, 0, 1, 65, 2, 822, 9, 11, 22, 3, 3, 3, 47]
    sorted1 = [0, 1, 2, 2, 3, 3, 3, 3, 9, 9, 9, 11, 22, 47, 65, 83, 822]
    assert quicksort(ls1) == sorted1
    # ls2 = [-6, 9, 0, 1, 17, 91, 0, 178]
    # sorted2 = [-6, 0, 0, 1, 9, 17, 91, 178]
    # assert quicksort(ls2) == sorted2
    # ls3 = [random.randint(0, 1000) for _ in range(1000)]
    # assert quicksort(ls3) == sorted(ls3)
