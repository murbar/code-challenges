'''
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/smallest-common-multiple

Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.
'''


def smallest_common_multiple(arr):
    a, b = min(arr), max(arr)
    scm = a * b

    while True:
        found = True
        # print(scm)
        for i in range(a, b+1):
            valid = scm % a == 0 and scm % b == 0 and scm % i == 0
            if not valid:
                found = False
                break

        if found:
            return scm
        else:
            scm += 1


assert smallest_common_multiple([1, 5]) == 60
assert smallest_common_multiple([5, 1]) == 60
assert smallest_common_multiple([2, 10]) == 2520
assert smallest_common_multiple([1, 13]) == 360360
assert smallest_common_multiple([23, 18]) == 6056820
