# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = int(''.join([i for i in str(abs(x))][::-1]))
        if rev > (2**31 - 1):
            return 0
        elif x < 0:
            return -rev
        else:
            return rev
