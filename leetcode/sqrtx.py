# https://leetcode.com/problems/sqrtx/


def mySqrt(self, x):
    lo, hi = 0, x

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid * mid > x:
            hi = mid - 1
        elif mid * mid < x:
            lo = mid + 1
        else:
            return mid

    # When there is no perfect square, hi is the the value on the left
    # of where it would have been (rounding down). If we were rounding up,
    # we would return lo
    return hi
