# https://leetcode.com/problems/find-peak-element/

# all elements preceding a peak are sorted smallest -> largest
# use binary search to find any peak in the array

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


s = Solution()
assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 1 or s.findPeakElement(
    [1, 2, 1, 3, 5, 6, 4]) == 5
