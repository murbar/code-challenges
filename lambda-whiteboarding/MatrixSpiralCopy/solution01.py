# Matrix Spiral Copy

# Given a 2D array(matrix) `inputMatrix` of integers, create a function
# `spiralCopy` that copies `inputMatrix`’s values into a 1D array in a clockwise
# spiral order. Your function then should return that array.

inputMatrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

output = [1, 2, 3, 4, 5, 10, 15, 20, 19,
          18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]


def spiralCopy(matrix):
    local_copy = [[*arr] for arr in matrix]
    total_elements = sum([len(arr) for arr in matrix])
    # matrix_length = len(matrix)
    # matrix_width = len(matrix[0])
    # assuming all sublists are of the same length
    result_list = []
    # for i in range(total_elements):
    while len(result_list) < total_elements:
        # step to the right, step down, step to the left, step up, repeat
        result_list.extend(local_copy[0])
        del local_copy[0]
        # step down
        for arr in local_copy:
            last_index = len(arr) - 1
            result_list.append(arr[last_index])
            del arr[last_index]
        # step left
        last_arr_index = len(local_copy) - 1
        result_list.extend(reversed(local_copy[last_arr_index]))
        del local_copy[last_arr_index]
        # step up
        for arr in reversed(local_copy):
            result_list.append(arr[0])
            del arr[0]

    return result_list


print(spiralCopy(inputMatrix))
print(output)

# ideally we'd want to not modify the input array and therefore not have to make a copy of it
# time complexity O(n) where n is the count of elements in the matrix
