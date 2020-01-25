'''
https://leetcode.com/problems/basic-calculator/
https://leetcode.com/problems/basic-calculator/discuss/62361/Iterative-Java-solution-with-stack/64037
'''

import doctest


class Solution:
    def calculate(self, s: str) -> int:
        '''
        >>> s = Solution()
        >>> s.calculate('(1+(4+5+2)-3) + (6+8)')
        23
        >>> s.calculate('(1+(4+5+26)-3) + (6+8)')
        47
        '''
        stack = []
        operand = 0
        result = 0
        sign = 1  # -1 when negative

        for ch in s:
            if ch.isdigit():
                # build the operand (value may be longer than one digit)
                operand = (operand * 10) + int(ch)

            elif ch in ('+', '-'):
                result += sign * operand
                sign = 1 if ch == '+' else -1
                # reset
                operand = 0

            elif ch == '(':
                # save for later
                stack.append(result)
                stack.append(sign)
                # reset for new sub-expression
                sign = 1
                result = 0

            elif ch == ')':
                result += sign * operand
                # get the sign
                result *= stack.pop()
                # then the operand
                result += stack.pop()
                operand = 0

        return result + sign * operand


class Solution2:
    def calculate(self, s: str) -> int:
        '''
        >>> s = Solution()
        >>> s.calculate('(1+(4+5+2)-3) + (6+8)')
        23
        >>> s.calculate('(1+(4+5+26)-3) + (6+8)')
        47
        '''
        operand = 0
        result = 0
        sign = 1  # -1 when negative
        stack = [sign]

        for ch in s:
            if ch.isdigit():
                # build the operand (value may be longer than one digit)
                operand = (operand * 10) + int(ch)

            elif ch in ('+', '-'):
                result += sign * operand
                sign = stack[-1] if ch == '+' else -stack[-1]
                # reset
                operand = 0

            elif ch == '(':
                stack.append(sign)

            elif ch == ')':
                stack.pop()

        return result + sign * operand


if __name__ == '__main__':
    doctest.testmod()
