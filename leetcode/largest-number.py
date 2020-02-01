# https://leetcode.com/problems/largest-number/


# sorting the list of nums is the key here
# we need to use a compare function to determine the larger of int(str1+str2) and int(str2+str1)
# quicksort is a good sort to show off here, not too complex
# then join the string values of the numbers, convert that to int (gets rid of leading zeros), then back to str

from typing import List


class Solution:
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    def partition(self, nums, l, r):
        pivot = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[pivot] = nums[pivot], nums[l]
                pivot += 1
            l += 1
        nums[pivot], nums[r] = nums[r], nums[pivot]
        return pivot

    def quicksort(self, nums, l, r):
        if l >= r:
            return
        pivot = self.partition(nums, l, r)
        self.quicksort(nums, l, pivot-1)
        self.quicksort(nums, pivot+1, r)

    def largestNumber(self, nums: List[int]) -> str:
        self.quicksort(nums, 0, len(nums)-1)
        return str(int(''.join(str(n) for n in nums)))


s = Solution()
s.largestNumber([3, 30, 34, 5, 9]) == "9534330"
s.largestNumber([10, 2]) == "210"
s.largestNumber([0, 0]) == "0"
