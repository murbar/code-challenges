# https://leetcode.com/problems/sort-colors/

# dutch partitioning problem https://en.wikipedia.org/wiki/Dutch_national_flag_problem
# sort array of colors red, white, blue (values 0, 1, 2) in-place
# pointers to keep track of first occurrences of 1 and 2?
# moving through the array, swap elements with another inside respective bounds
# 0s move to the front, 2s to the back, 1s in between the two pointers of where 1s begin and end

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2-pass count, O(n) time, O(1) space
        RED, WHITE, BLUE = 0, 1, 2
        n_red = 0
        n_white = 0

        for c in nums:
            if c == RED:
                n_red += 1
            elif c == WHITE:
                n_white += 1

        for i in range(len(nums)):
            if i < n_red:
                nums[i] = RED
            elif i >= n_white + n_red:
                nums[i] = BLUE
            else:
                nums[i] = WHITE

    def sortColors2(self, nums: List[int]) -> None:
        # "single pass" although we see some elements more than once
        RED, WHITE, BLUE = 0, 1, 2
        start = 0
        end = len(nums) - 1
        current = 0

        while current <= end and start < end:
            # stack reds at beginning of array
            if nums[current] == RED:
                # swap current (red) and start
                nums[current] = nums[start]
                nums[start] = RED
                start += 1
                current += 1
            # blues at the end of array
            elif nums[current] == BLUE:
                # swap current (blue) and end
                nums[current] = nums[end]
                nums[end] = BLUE
                # value at end could be any of the three
                # leave current unchanged so we can process it on the next iteration
                end -= 1
            # whites will fall to the middle
            # just move to next element
            else:
                current += 1

    def sortColors3(self, nums: List[int]) -> None:
        '''This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified, and blue. Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.

        If the white pointer is red(nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. If the pointer is white(nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. If the white pointer is blue, we swap with the latest unclassified element.'''

        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


s = Solution()
l1 = [2, 0, 2, 1, 1, 0]
s.sortColors(l1)
assert l1 == [0, 0, 1, 1, 2, 2]
l2 = [1, 1, 1, 1, 2, 2, 1, 2, 0, 2, 0, 0, 0, 1, 1, 2, 1, 1, 1, 2, 1]
s.sortColors(l2)
assert l2 == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

l3 = [2, 0, 2, 1, 1, 0]
s.sortColors(l3)
assert l3 == [0, 0, 1, 1, 2, 2]
l4 = [1, 1, 1, 1, 2, 2, 1, 2, 0, 2, 0, 0, 0, 1, 1, 2, 1, 1, 1, 2, 1]
s.sortColors2(l4)
assert l4 == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

l5 = [1, 1, 1, 1, 2, 2, 1, 2, 0, 2, 0, 0, 0, 1, 1, 2, 1, 1, 1, 2, 1]
s.sortColors3(l5)
assert l5 == [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

l6 = [1, 0, 0, 1, 1, 1, 0, 1, 1]
s.sortColors3(l6)
assert l6 == [0, 0, 0, 1, 1, 1, 1, 1, 1]
