# https://leetcode.com/problems/power-of-three/


# if 3 goes into n evenly, divide by 3 until it does not
# if n is now 1, return true

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1
