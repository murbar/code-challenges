# https://leetcode.com/problems/happy-number/

# if we ever see the same output from sum_of_sqrs twice, we're in a cycle, return False


class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_sqrs(number):
            # return sum(int(n)**2 for n in list(str(number)))
            s = 0
            while number != 0:
                last = number % 10
                s += last * last
                # truncate last digit
                number //= 10
            return s

        seen = set()
        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = sum_of_sqrs(n)

        return True


s = Solution()
assert s.isHappy(18) == False
assert s.isHappy(19) == True
