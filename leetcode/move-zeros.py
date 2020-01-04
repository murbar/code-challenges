# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n) time (2n worst case all zeros), O(1) space, good enough
        non_zero_i = 0

        for n in nums:
            if n != 0:
                nums[non_zero_i] = n
                non_zero_i += 1

        for i in range(non_zero_i, len(nums)):
            nums[i] = 0


s = Solution()
s.moveZeroes([0, 0, 0, 0, 0])
