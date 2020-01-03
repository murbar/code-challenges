# https://leetcode.com/problems/rotate-array/

# best solution uses in-place reverse
# k = k % len(array) to account for k larger than array length
# [1, 2, 3, 4, 5, 6, 7] k = 3
# [7, 6, 5, 4, 3, 2, 1] reverse whole array
# [5, 6, 7, 4, 3, 2, 1] reverse first k elements
# [5, 6, 7, 1, 2, 3, 4] reverse the remaining elements


class Solution:
    def rotate(self, nums, k) -> None:
        # brute force
        for _ in range(k):
            n = nums.pop()
            nums.insert(0, n)
        print(nums)

    def rotate2(self, nums, k) -> None:
        # extra array, O(n) time & space
        temp = [0] * len(nums)

        for i in range(len(nums)):
            j = (i + k) % len(nums)
            temp[j] = nums[i]

        for i in range(len(nums)):
            nums[i] = temp[i]

    def rotate3(self, nums, k) -> None:
        # in-place, O(n) time, O(1) space
        def reverse(arr, i, j):
            '''Reverse elements of arr from indexes i to j'''
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        k %= len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
