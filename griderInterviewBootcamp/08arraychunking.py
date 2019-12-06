# chunk([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]


def chunk(arr, size):
    result = []

    for i in range(0, len(arr), size):
        result.append(arr[i:i+size])

    return result


assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
assert chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) == [[1, 2, 3], [4, 5, 6], [7, 8]]
assert chunk([1, 2, 3, 4, 5], 4) == [[1, 2, 3, 4], [5]]
assert chunk([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
print('All tests passed!')
