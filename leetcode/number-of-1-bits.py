# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:]
        return sum(int(b) for b in bits)
