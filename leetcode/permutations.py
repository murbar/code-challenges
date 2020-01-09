# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def recur(done, remaining):
            if len(done) == len(nums):
                results.append(done)
            else:
                for n in remaining:
                    r = remaining.copy()
                    r.remove(n)
                    recur(done + [n], r)

        recur([], nums)
        return results

    def permute2(self, nums: List[int]) -> List[List[int]]:
        # modified recur function
        results = []

        def recur(nums, result):
            if not nums:
                results.append(result)
            else:
                for i in range(len(nums)):
                    recur(nums[:i] + nums[i+1:], result + [nums[i]])

        recur(nums, [])
        return results


s = Solution()
assert s.permute([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
assert s.permute([]) == [[]]
assert s.permute2([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1]
]
assert s.permute2([]) == [[]]
