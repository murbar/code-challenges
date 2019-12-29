# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i, j = 0, 0
        last = nums[i]

        while i < len(nums):
            curr = nums[i]
            if curr != last:
                j += 1
                nums[j] = curr

            i += 1
            last = curr

        return j+1
