# https://leetcode.com/problems/maximum-subarray/
# https://www.youtube.com/watch?v=tinz1fiYv0c


from typing import List


class Solution:
    # No need to hold all previous maxes in a DP sub-array, just track the current max.
    # def maxSubArray(self, nums: List[int]) -> int:
    #     sums = [0] * len(nums)
    #     max_sum = nums[0]
    #     sums[0] = max_sum

    #     for i in range(1, len(nums)):
    #         curr = nums[i]
    #         sums[i] = max(curr, curr + sums[i-1])
    #         max_sum = max(max_sum, sums[i])

    #     return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            global_max = max(current_max, global_max)

        return global_max


s = Solution()
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
