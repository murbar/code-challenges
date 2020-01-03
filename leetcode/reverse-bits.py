# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        reversed_ = bits[::-1]
        padded = reversed_.ljust(32, '0')
        return int(padded, 2)
