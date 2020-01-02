# https://leetcode.com/problems/excel-sheet-column-number/


def letter_to_num(l):
    return ord(l.lower()) - ord('a') + 1


class Solution:
    def titleToNumber(self, s: str) -> int:
        base = 26
        number = 0
        # step backwards over chars in s
        for i, letter in enumerate(list(s)[::-1]):
            # n in place i will be n * base^i
            # eg. 520, base 10
            # for n = 2, 2 == 2 * 10^1
            # for n = 5, 5 == 5 * 10^2
            # eg. 'CB', base 26
            # C == 3 * 26^1 == 78, B == 2 * 26^0 == 2, CB == 80
            multiplier = base ** i
            number += letter_to_num(letter) * multiplier

        return number


s = Solution()
assert s.titleToNumber('CB') == 80
assert s.titleToNumber('A') == 1
assert s.titleToNumber('ZY') == 701
