# https://leetcode.com/problems/climbing-stairs/

# very similar to fibonacci, with n == itself when less than 3


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(n):
            if n < 3:
                return n

            if not n in cache:
                cache[n] = helper(n-1) + helper(n-2)
            return cache[n]

        return helper(n)
