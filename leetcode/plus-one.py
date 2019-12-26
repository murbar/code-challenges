# https://leetcode.com/problems/plus-one/


class Solution:
    # slow
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(n) for n in digits]))
        num += 1
        return [int(n) for n in str(num)]

    # improved
    def plusOne2(self, digits: List[int]) -> List[int]:
        # work backward through the list of digits
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1

            # done trickling up, break out of the loop
            if digits[i] != 0:
                return digits

        # all digits are now 0, prepend 1
        return [1] + digits
