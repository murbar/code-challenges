# https://leetcode.com/problems/power-of-three/


# if 3 goes into n evenly, divide by 3 until it does not
# if n is now 1, return true

# can be done with multiplication too

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1

    def isPowerOfThree2(self, n: int) -> bool:
        if n < 1:
            return False

        i = 1
        while i < n:
            i *= 3

        return i == n


s = Solution()
assert s.isPowerOfThree(27) == True
assert s.isPowerOfThree(0) == False
assert s.isPowerOfThree(9) == True
assert s.isPowerOfThree(45) == False
assert s.isPowerOfThree2(27) == True
assert s.isPowerOfThree2(0) == False
assert s.isPowerOfThree2(9) == True
assert s.isPowerOfThree2(45) == False
