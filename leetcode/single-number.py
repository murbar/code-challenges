# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)

        return seen.pop()

    def singleNumber2(self, nums: List[int]) -> int:
        # fancy math
        # 2 * (a + b + c) - (a + a + b + b + c) == c
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums: List[int]) -> int:
        # XOR of 0 and n is n
        # XOR of n and n is 0
        # a ^ b ^ a == 0 ^ b == b
        r = 0
        for n in nums:
            r ^= n
        return r
