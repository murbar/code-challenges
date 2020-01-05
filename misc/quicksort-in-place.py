

def quicksort(ls, low=0, high=None):
    if high is None:
        high = len(ls)

    if low >= high:
        return ls

    else:
        pivot_i = low
        for i in range(low, high):
            if ls[i] < ls[pivot_i]:
                ls[i], ls[pivot_i+1] = ls[pivot_i+1], ls[i]
                ls[pivot_i], ls[pivot_i+1] = ls[pivot_i+1], ls[pivot_i]
                pivot_i += 1

        ls = quicksort(ls, low, pivot_i)
        ls = quicksort(ls, pivot_i+1, high)

        return ls


if __name__ == '__main__':
    ls1 = [9, 3, 83, 9, 2, 0, 1, 65, 2, 822, 9, 11, 22, 3, 3, 3, 47]
    sorted1 = [0, 1, 2, 2, 3, 3, 3, 3, 9, 9, 9, 11, 22, 47, 65, 83, 822]
    assert quicksort(ls1) == sorted1
    ls2 = [-6, 9, 0, 1, 17, 91, 0, 178]
    sorted2 = [-6, 0, 0, 1, 9, 17, 91, 178]
    assert quicksort(ls2) == sorted2
    import random
    ls3 = [random.randint(0, 1000) for _ in range(1000)]
    assert quicksort(ls3) == sorted(ls3)
