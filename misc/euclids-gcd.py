
'''
What is the GCD of 56 and 12?

Step 1 - Divide the larger by the smaller number:-

56 / 12 = 4 (remainder 8)

Step 2 - Divide the divisor by the remainder from the previous step:-

12 / 8 = 1 (remainder 4)

Step 3 - Continue step 2 until no remainders are left (in this case it's a simple 3 step process):-

8 / 4 = 2 (no remainder)

In this case, the GCD is 4.
'''


def euclids(x, y):
    if x < y:
        return euclids(y, x)

    while y != 0:
        x, y = y, x % y

    return x


if __name__ == '__main__':
    assert euclids(56, 12) == 4
    assert euclids(150, 304) == 2
