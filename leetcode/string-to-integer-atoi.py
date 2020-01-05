# https://leetcode.com/problems/string-to-integer-atoi/

import re

# whitespace is ' '
# starts with optional witespace of any size
# then optional + or -
# then any number of digits
# then any other arbitrary chars

# can be done without call to int() but that's silly


class Solution:
    def myAtoi(self, num_str: str) -> int:
        # ^\s* - starts with zero or more whitespace
        # () - capture group
        # [+|-]? - optional '+' or '-'
        # \d+ - one or more digits
        r = re.compile(r'\s*([+|-]?\d+)')
        match = r.match(num_str)

        if not match:
            return 0

        # group 0 is entire matching string, 1 is first group
        n = int(match.group(1))

        if n.bit_length() >= 32:
            return 2**31 - 1 if n > 0 else -2**31

        return n

    def myAtoi2(self, num_str: str) -> int:
        # without regex
        num_str = num_str.strip()
        if not num_str:
            return 0

        value = ''

        if num_str[0] in '+-':
            value = num_str[0]
            num_str = num_str[1:]

        for ch in num_str:
            if ch.isdigit():
                value += ch
            else:
                break

        try:
            num = int(value)
            if num.bit_length() >= 32:
                return 2**31 - 1 if num > 0 else -2**31

            return num

        except ValueError:
            return 0


s = Solution()
assert s.myAtoi("42") == 42
assert s.myAtoi("-91283472332 asdf") == -2**31
assert s.myAtoi("4193 with words") == 4193
assert s.myAtoi("   -42") == -42
assert s.myAtoi(" +90") == 90
assert s.myAtoi("words and 987") == 0
assert s.myAtoi2("42") == 42
assert s.myAtoi2("-91283472332 asdf") == -2**31
assert s.myAtoi2("4193 with words") == 4193
assert s.myAtoi2("   -42") == -42
assert s.myAtoi2(" +90") == 90
assert s.myAtoi2("words and 987") == 0
