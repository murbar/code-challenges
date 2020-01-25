'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Reminds me of Dijkstra's two-stack algo for evaluating infix expressions. My first idea was to use a stack for values and a queue for ops. But since an op is applied to the two values before it, we don't need to collect the ops, just apply them to value on a stack until we reach the end of the list.

- Move through the list, add value to stack until we find an operator.
- Pop last two values off stack, eval with op, and put result back on stack.
- Last token in input should always be an op due to reverse notation.
- There should always be two values on the stack at that point because as inputs are guaranteed to be valid.
'''


from typing import List
import doctest


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        >>> s = Solution()
        >>> s.evalRPN(['2', '1', '+', '3', '*'])
        9
        >>> s.evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
        22
        >>> s.evalRPN(['4', '13', '5', '/', '+'])
        6
        '''
        ops_map = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            # round down - floor division doesn't quite work
            # eg. 6 // -132 == floor(-0.4...) == -1, no good
            '/': lambda a, b: int(a / b)
        }
        stack = []

        for token in tokens:
            if token not in ops_map:
                stack.append(token)
            else:
                # b then a, we added to stack in reverse order
                # important for subtraction/division
                b = int(stack.pop())
                a = int(stack.pop())
                result = ops_map[token](a, b)
                stack.append(result)

        return stack[0]


class Solution2:
    '''
    Inside-out: scan the list until we find two values followed by an operator. Stop and eval that sub expression, sub result in place of expression. Scan again until list contains one value. This should work because this are n-1 ops for a list with n values. Not very efficient due to slicing and coping of lists. Impractical for large inputs.
    '''

    def evalRPN(self, tokens: List[str]) -> int:
        ops_map = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            # round down - floor division doesn't quite work
            # eg. 6 // -132 == floor(-0.4...) == -1, no good
            '/': lambda a, b: int(a / b)
        }

        # while there are two values and an operator
        # valid expressions with have n-1 ops for n values
        while len(tokens) > 1:
            i = 0
            # keep i at 3rd from last position
            while i <= len(tokens) - 3:
                a, b, op = tokens[i:i+3]
                # check a is int, b is int, and op is op
                if op in ops_map and a not in ops_map and b not in ops_map:
                    result = ops_map[op](int(a), int(b))
                    tokens = tokens[:i] + [result] + tokens[i+3:]
                else:
                    i += 1

        return tokens[0]


if __name__ == '__main__':
    doctest.testmod()
