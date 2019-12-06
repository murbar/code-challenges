# chunk([1, 2, 3, 4, 5], 2) -> [[1, 2], [3, 4], [5]]


def chunk(arr, size):
    chunked = []

    for i in range(0, len(arr), size):
        stop = i + size
        chunked.append(arr[i:stop])

    return chunked


def chunk2(arr, size):
    chunked = []

    for el in arr:
        if not len(chunked):
            chunked.append([])

        last_chunk = chunked[-1]
        if len(last_chunk) < size:
            last_chunk.append(el)
        else:
            chunked.append([el])

    return chunked


assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
assert chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) == [[1, 2, 3], [4, 5, 6], [7, 8]]
assert chunk([1, 2, 3, 4, 5], 4) == [[1, 2, 3, 4], [5]]
assert chunk([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
assert chunk2([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
assert chunk2([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
assert chunk2([1, 2, 3, 4, 5, 6, 7, 8], 3) == [[1, 2, 3], [4, 5, 6], [7, 8]]
assert chunk2([1, 2, 3, 4, 5], 4) == [[1, 2, 3, 4], [5]]
assert chunk2([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
print('All tests passed!')
