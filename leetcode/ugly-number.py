# https://leetcode.com/problems/ugly-number/

# Ugly numbers are positive numbers whose prime factors only include 2, 3, or 5

# my initial intuition was to search for any factor that wasn't 1, n, 2, 3, or 5
# that doesn't work since we are looking for PRIME factors only


class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        factors = (2, 3, 5)

        for f in factors:
            # if num has factor, "take it out" until it doesn't
            while num % f == 0:
                num //= f

        # after factoring out primes, num == 1 unless there are other prime factors
        return num == 1


s = Solution()
assert s.isUgly(6) == True
assert s.isUgly(1) == True
assert s.isUgly(8) == True
assert s.isUgly(14) == False
assert s.isUgly(0) == False
