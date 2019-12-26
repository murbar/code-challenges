# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in cache:
                return [cache[needed], i]
            cache[num] = i
