# https://leetcode.com/problems/find-peak-element/

# all elements preceding a peak are sorted smallest -> largest
# nums[i] and nums[i+1] are never equal
# use binary search to find "any peak"in the array

from typing import List


class Solution:
    # O(lg n) time, O(1) space
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


class SolutionRecursive:
    # O(lg n) time and space (extra space for call stack)
    def search(self, nums, left, right):
        if left == right:
            return left

        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            return self.search(nums, mid+1, right)

        return self.search(nums, left, mid)

    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums)-1)


s = Solution()
sr = SolutionRecursive()
assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 1 or s.findPeakElement(
    [1, 2, 1, 3, 5, 6, 4]) == 5
assert sr.findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 1 or sr.findPeakElement(
    [1, 2, 1, 3, 5, 6, 4]) == 5
