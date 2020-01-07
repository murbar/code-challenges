# https://leetcode.com/problems/divide-two-integers/

# divide without using multiplication, division or mod operators
# result must be 32-bit (less than 2^31 - 1)
# divisor will never be zero
# could subtract until num is less than divisor, return num subtractions
# bit manipulation?
# binary search?


def negate(n):
    return n - n - n


assert negate(0) == 0
assert negate(-3) == 3
assert negate(3) == -3

MIN32 = -2 ** 31
MAX32 = 2 ** 31 - 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # naive approach, too slow with large dividend and small divisor
        if divisor == 1:
            return dividend

        subtractions = 0

        # result is negative if either the dividend or divisor is negative, but not both
        is_negative = (dividend < 0) != (divisor < 0)

        # make both positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend > divisor:
            dividend -= divisor
            subtractions += 1

        return -subtractions if is_negative else subtractions

    def divide2(self, dividend: int, divisor: int) -> int:
        # speed it up by increasing the divisor while it is less than dividend
        # and decreasing it as needed

        # result is negative if either the dividend or divisor is negative, but not both
        is_negative = (dividend < 0) != (divisor < 0)

        # make both positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        total = divisor

        # increment running total until it is larger than dividend
        # this loop cuts our work in half each iteration
        while total <= dividend:
            current_quotient = 1
            # double the amount of increment until it's larger than dividend
            while (total + total) <= dividend:
                total += total
                # order of quotient tracks order of total
                current_quotient += current_quotient
            # this line cuts dividend by about half of its current value
            dividend -= total
            # reset total to divisor for next iteration
            total = divisor
            # accumulate current quotient
            quotient += current_quotient

        # negate quotient if result should be negative
        if is_negative:
            quotient = -quotient

        # check for 32-bit min and max
        if quotient < MIN32:
            return MIN32

        if quotient > MAX32:
            return MAX32

        return quotient

    def divide3(self, dividend: int, divisor: int) -> int:
        # with bitwise ops, basically the same as solution above
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            # << 1 doubles a number, >> 1 halves it (integer division by 2)
            # by shifting bits by 1 power of 2
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))


s = Solution()
assert s.divide(10, 3) == 3
assert s.divide(10, -3) == -3
assert s.divide(-10, -3) == 3
assert s.divide(20000000, 3) == 6666666
assert s.divide2(10, 3) == 3
assert s.divide2(10, -3) == -3
assert s.divide2(-10, -3) == 3
assert s.divide2(20000000, 3) == 6666666
