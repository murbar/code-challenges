# https://leetcode.com/problems/powx-n/

# iterative or recursive
# x^n :: 1 / x^(-n), n is negative
#        x * x^(n-1), n is odd
#        x^(n/2) * x^(n/2), n is even
#        1, n == 0

# what about float precision?
# turns out n/a for leetcode tests


def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n:
        # n is odd, equivalent to n % 2 == 1
        if n & 1:
            result *= x
        x *= x
        # halve n
        n >>= 1
    return result


def myPowR(x: float, n: int) -> float:
    if n == 0:
        return 1
    # n is negative, 1 / x^(-n): 2^(-2) = 1/2^2 = 1/4 = 0.25
    if n < 0:
        return 1 / myPowR(x, -n)
    # n is even, x^(n/2) * x^(n/2)
    if n % 2 == 0:
        return myPowR(x*x, n/2)
    # n is odd
    return x * myPowR(x, n-1)


assert myPow(2.0, 10) == 1024.00
# fails assertion due to float precision -> 9.261000000000001
# passes on leetcode
# assert myPow(2.1, 3) == 9.26100
assert myPow(2.0, -2) == 0.25
assert myPowR(2.0, 10) == 1024.00
# fails assertion due to float precision -> 9.261000000000001
# assert myPowR(2.1, 3) == 9.26100
assert myPowR(2.0, -2) == 0.25
