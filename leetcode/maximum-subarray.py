# https://leetcode.com/problems/maximum-subarray/
# https://www.youtube.com/watch?v=tinz1fiYv0c


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [0] * len(nums)
        max_sum = nums[0]
        sums[0] = max_sum

        for i in range(1, len(nums)):
            curr = nums[i]
            sums[i] = max(curr, curr + sums[i-1])
            max_sum = max(max_sum, sums[i])

        return max_sum
