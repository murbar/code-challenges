# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# all signs point to binary search
# "O(lg n)", "sorted", "target"
# repeat with two sub arrays on either side of target until boundaries are
# at first and last position of values equal to target
# O(3 log n) -> O (log n)

# https://www.youtube.com/watch?v=bU-q1OJ0KWw

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        not_found = [-1, -1]
        if not list:
            return not_found

        # b-search for target
        left, right = 0, len(nums) - 1
        target_i = -1
        while left <= right and target_i == -1:
            mid = (left + right) // 2
            if nums[mid] == target:
                target_i = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # target not found? bail
        if target_i == -1:
            return not_found

        # reset and search for left bound in elements before target index
        left = 0
        right = target_i
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            else:
                left = mid + 1

        # start is at left or the position after it
        start = left if nums[left] == target else left + 1

        # reset and search for right bound in elements after target index
        left = target_i
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            else:
                right = mid - 1

        # end is at right or the position before it
        end = right if nums[right] == target else right - 1

        return [start, end]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        # much simplified
        # modified binary search finds the bounds
        # keep looking until right == left AND left and right contain an index that points to target
        # if target == num[mid], we need to recur on one of two sides of the array
        # left side flag tells us which side to process, if True, go left, else right
        # left bound will never occur at position after where target was located
        # conversely for the right bound, never occurs before position of target
        # O(2 lg n) -> O(lg n)
        # this might be two functions without "is left" the flag
        def find_boundary(ls, target, left_side=True):
            left, right = 0, len(ls)

            while left < right:
                mid = (left + right) // 2
                # first condition for searching right side, second in case of left side
                if nums[mid] > target or (left_side and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1

            return left

        start = find_boundary(nums, target)
        # if target not in array, start will be out of bounds or it won't point to a target
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = find_boundary(nums, target, False) - 1

        return [start, end]

    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        # a slightly more straight-forward implementation
        # search function looks more like a regular binary search
        # could be two functions, search_left & search_right
        # instead of only equality, we look for equality and < or >
        def find_boundary(ls, target, is_left_side):
            index = -1
            left, right = 0, len(ls) - 1
            while left <= right:
                mid = (left + right) // 2

                # different comparison depending on which side we're searching
                if is_left_side:
                    if nums[mid] >= target:
                        right = mid - 1
                    else:
                        left = mid + 1
                # right side, similar but inverse operations
                else:
                    if nums[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid - 1

                # if target not in array, index will remain -1
                if nums[mid] == target:
                    index = mid

            return index

        # search once for each boundary
        start = find_boundary(nums, target, True)
        end = find_boundary(nums, target, False)
        return [start, end]


s = Solution()
assert s.searchRange([5, 7, 7, 8, 8, 10], 7) == [1, 2]
assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert s.searchRange([5, 8, 8, 8, 8, 10], 8) == [1, 4]
assert s.searchRange([8, 8], 8) == [0, 1]
assert s.searchRange([8, 8], 9) == [-1, -1]
assert s.searchRange([8], 9) == [-1, -1]
assert s.searchRange([], 9) == [-1, -1]
assert s.searchRange([8], 8) == [0, 0]
assert s.searchRange([8, 8, 8, 8], 8) == [0, 3]
assert s.searchRange([1, 4], 1) == [0, 0]
assert s.searchRange([1, 4], 4) == [1, 1]

assert s.searchRange2([5, 7, 7, 8, 8, 10], 7) == [1, 2]
assert s.searchRange2([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert s.searchRange2([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert s.searchRange2([5, 8, 8, 8, 8, 10], 8) == [1, 4]
assert s.searchRange2([8, 8], 8) == [0, 1]
assert s.searchRange2([8, 8], 9) == [-1, -1]
assert s.searchRange2([8], 9) == [-1, -1]
assert s.searchRange2([], 9) == [-1, -1]
assert s.searchRange2([8], 8) == [0, 0]
assert s.searchRange2([8, 8, 8, 8], 8) == [0, 3]
assert s.searchRange2([1, 4], 1) == [0, 0]
assert s.searchRange2([1, 4], 4) == [1, 1]

assert s.searchRange3([5, 7, 7, 8, 8, 10], 7) == [1, 2]
assert s.searchRange3([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert s.searchRange3([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert s.searchRange3([5, 8, 8, 8, 8, 10], 8) == [1, 4]
assert s.searchRange3([8, 8], 8) == [0, 1]
assert s.searchRange3([8, 8], 9) == [-1, -1]
assert s.searchRange3([8], 9) == [-1, -1]
assert s.searchRange3([], 9) == [-1, -1]
assert s.searchRange3([8], 8) == [0, 0]
assert s.searchRange3([8, 8, 8, 8], 8) == [0, 3]
assert s.searchRange3([1, 4], 1) == [0, 0]
assert s.searchRange3([1, 4], 4) == [1, 1]
