# O(n^2)
# for each element, set it as smallest element, then iterate trough remaining items
# and if we find a smaller value, swap the position of the two elements


def selection_sort(ls):
    for i in range(len(ls)):
        min_index = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        if i != min_index:
            ls[i], ls[min_index] = ls[min_index], ls[i]

    return ls


assert selection_sort([5, 8, 4, 9, 1]) == [1, 4, 5, 8, 9]
assert selection_sort([10, 0, 97, -30, 5]) == [-30, 0, 5, 10, 97]
print('All tests passed!')
