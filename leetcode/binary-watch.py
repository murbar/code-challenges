# https://leetcode.com/problems/binary-watch/

# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

# this is basically an array permutation problem
# represent bits as minutes
# hours 8, 4, 2, 1 minutes, 32, 16 ...
# (480, 240, 120, 60, 32, 16, 8, 4, 2, 1)
# for n == 2 get permutations of bit array with two bits on and 8 off
# map on bits to minutes map add them up and that's one possible time
# seems like there must be a much more efficient way to find the permutations
# could use itertools

# how about iterating over each minute in the day and computing the number of bits
# needed to represent it?

from itertools import combinations
from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # using itertools
        bit_map = (480, 240, 120, 60, 32, 16, 8, 4, 2, 1)
        times = []

        for combo in combinations(bit_map, num):
            hrs, mins = divmod(sum(combo), 60)
            if hrs > 11:
                continue
            times.append(f'{hrs}:{mins:02}')
        return times

    def readBinaryWatch2(self, num: int) -> List[str]:
        # no libraries
        # iterate over each minute of the day
        # count the number of bits set for that time
        # constant time and space
        times = []

        for h in range(12):
            for m in range(60):
                bit_string = bin(h) + bin(m)
                if bit_string.count('1') == num:
                    times.append(f'{h}:{m:02}')

        return times


s = Solution()
print(s.readBinaryWatch(5))
assert s.readBinaryWatch(1) == [
    '8:00', '4:00', '2:00', '1:00', '0:32', '0:16', '0:08', '0:04', '0:02', '0:01']
assert s.readBinaryWatch2(1) == [
    '0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']
