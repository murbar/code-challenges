'''
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/smallest-common-multiple

Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.

- Key is to increment the SCM by the max of the range after each check (SCM must be a multiple of max, so max is minium increment)
'''


def smallest_common_multiple(arr):
    a, b = min(arr), max(arr)
    scm = a * b

    while True:
        found = True

        for i in range(a, b+1):
            valid = scm % a == 0 and scm % b == 0 and scm % i == 0
            if not valid:
                found = False
                break

        if found:
            return scm
        else:
            scm += b


def smallest_common_multiple2(arr):
    a, b = min(arr), max(arr)
    scm = b

    def is_valid(m, min_, max_):
        for i in range(min_, max_):
            if m % i != 0:
                return False

        return True

    while not is_valid(scm, a, b):
        scm += b

    return scm


assert smallest_common_multiple([1, 5]) == 60
assert smallest_common_multiple([5, 1]) == 60
assert smallest_common_multiple([2, 10]) == 2520
assert smallest_common_multiple([1, 13]) == 360360
assert smallest_common_multiple([23, 18]) == 6056820

assert smallest_common_multiple2([1, 5]) == 60
assert smallest_common_multiple2([5, 1]) == 60
assert smallest_common_multiple2([2, 10]) == 2520
assert smallest_common_multiple2([1, 13]) == 360360
assert smallest_common_multiple2([23, 18]) == 6056820
