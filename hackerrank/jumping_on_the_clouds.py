# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

# input
# 7
# 0 0 1 0 0 1 0

# output
# 4

# import math
# import os
# import random
# import re
# import sys


def jumpingOnClouds(c):
    currentIndex = 0
    lastIndex = len(c) - 1
    hops = 0

    while currentIndex < lastIndex:
        next1, next2 = currentIndex + 1, currentIndex + 2
        next2_in_bounds = next2 <= lastIndex
        next2_is_cumulus = c[next2] == 0 if next2_in_bounds else False
        if next2_in_bounds and next2_is_cumulus:
            currentIndex = next2
            hops += 1
        else:
            currentIndex = next1
            hops += 1

    return hops


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(raw_input())
#     c = map(int, raw_input().rstrip().split())
#     result = jumpingOnClouds(c)
#     fptr.write(str(result) + '\n')
#     fptr.close()


print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
