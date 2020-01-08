# https://leetcode.com/problems/search-in-rotated-sorted-array/

# binary search in a sorted array
# but the array is rotated at an arbitrary pivot
# no dupes
# return index of target or -1 if not present
# must solve with O(log n)

# traverse array once to locate the pivot at position n
# use n to translate i in binary search
# might as well just look for the target if we are traversing the array
# increases time complexity to O(n log n) - too large...

# efficient solution involves two searches - first for the pivot location
# pivot is smallest element in array, by definition
# then again for the target - O(2 log n) -> O(log n)
# could translate the pivot and search the whole array or
# search either side of pivot based on value of target

from typing import List


class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        # check for empty lists
        if not nums:
            return -1

        # helper to perform b-search
        def binary_search(ls, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if ls[mid] == target:
                    return mid
                elif target > ls[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        left, right = 0, len(nums) - 1
        # if last element is greater than first, this array isn't rotated
        # search for the target right away
        if nums[left] < nums[right]:
            return binary_search(nums, target, left, right)

        # locate the pivot with modified binary search
        # right will approach and land at the largest element
        # left will be the smallest - that's the pivot
        while left < right:
            mid = (left + right) // 2
            # if mid is greater than last element, we are still in the rotated portion of the list
            if nums[mid] > nums[right]:
                left = mid + 1
            # if not, search back half of array
            else:
                right = mid

        # left is now smallest element in the array
        pivot = left

        # if the pivot the target?
        if nums[pivot] == target:
            return pivot
        # if not, search for target on either side of the pivot
        elif target <= nums[-1]:
            # target is smaller than last element, search the back half of the array
            return binary_search(nums, target, pivot+1, len(nums)-1)
        else:
            # target is greater than last element, search the front half
            return binary_search(nums, target, 0, pivot-1)

    def search(self, nums: List[int], target: int) -> int:
        # slightly different structure, same approach as above
        # helps with fully grokking the algorithm
        # helper function not really necessary for this problem
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        # locate pivot
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        # reset
        left, right = 0, len(nums)-1
        # determine bounds of binary search to locate target
        if target >= nums[pivot] and target <= nums[right]:
            # search from pivot to right
            left = pivot
        else:
            # from left to pivot
            right = pivot
        # locate target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                # target found
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # target not in array
        return -1


s = Solution()
assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert s.search([1, 5], 5) == 1
assert s.search([1, 5], 1) == 0
assert s.search([5, 1], 1) == 1
assert s.search([5, 1], 5) == 0
assert s.search([1, 3], 0) == -1
assert s.search([], 5) == -1
assert s.search([1], 0) == -1
