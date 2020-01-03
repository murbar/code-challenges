# https://leetcode.com/problems/factorial-trailing-zeroes/

# had to look this up, wouldn't have come up with this formula on my own

'''
https://www.purplemath.com/modules/factzero.htm

5s pair with 2s from even factors to give us factors os 10.

Take the number that you've been given the factorial of.
Divide by 5; if you get a decimal, truncate to a whole number.
Divide by 5^2 = 25; if you get a decimal, truncate to a whole number.
Divide by 5^3 = 125; if you get a decimal, truncate to a whole number.
Continue with ever-higher powers of 5, until your division results in a number less than 1. Once the division is less than 1, stop.
Sum all the whole numbers you got in your divisions. This is the number of trailing zeroes.

By the way, you can get the same result, if you keep track as you go, by just dividing repeatedly in your calculator by 5's: 4617 ÷ 5 = 923.4 (write down 923), 923.4 ÷ 5 = 184.68 (write down 184), 184.68 ÷ 5 = 36.936 (write down 36), 36.936 ÷ 5 = 7.3827 (write down 7), 7.3827 ÷ 5 = 1.47744 (write down 1), and 1.47744 ÷ 5 is going to be less than 1, so you're done. Turn to your scratch paper were you've written down the whole numbers, and sum them to get 1151.
'''


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        factor = 5
        while factor <= n:
            zeros += n // factor
            factor *= 5

        return zeros

    def trailingZeroesAlt(self, n):
        zeros = 0
        while n > 1:
            n /= 5  # n = n / 5
            zeros += int(n)

        return zeros


s = Solution()
assert s.trailingZeroes(5) == 1
assert s.trailingZeroes(23) == 4
assert s.trailingZeroes(101) == 24
assert s.trailingZeroes(1000) == 249
assert s.trailingZeroes(4617) == 1151
assert s.trailingZeroesAlt(5) == 1
assert s.trailingZeroesAlt(23) == 4
assert s.trailingZeroesAlt(101) == 24
assert s.trailingZeroesAlt(1000) == 249
assert s.trailingZeroesAlt(4617) == 1151
