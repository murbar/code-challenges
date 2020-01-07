# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# seems like we'll need recursive backtracking, similar to the phone letter combos problem
# each single paren should occur n times in a result string size 2n
# check each result for well-formed pairs before adding to results list?
# possible to generate only valid results?

from typing import List


def well_formed(s):
    # keep track of open parens
    opens = 0
    for ch in s:
        if ch == '(':
            opens += 1
        else:
            # if none open, invalid - can't close before opening
            if not opens:
                return False
            # pair is matched, remove opening from stack
            opens -= 1
    # all opens should be closed, opens should be 0
    return not opens


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # generate all permutations and validate before adding to result list
        result = []

        def recur(current=''):
            # if length of current is 2n, stop recursing
            if len(current) == 2 * n:
                # is current valid?
                if well_formed(current):
                    result.append(current)
                return

            # always being with '('
            if current == '':
                recur('(')
            else:
                # each result will have n '(' and n ')'
                for p in ('(', ')'):
                    if current.count(p) < n:
                        recur(current + p)

        recur()
        return result

    def generateParenthesis2(self, n: int) -> List[str]:
        # generating only valid result, no need to validate
        # keep count of opening and closing parens at each recursive call
        result = []

        def recur(current='', n_open=0, n_close=0):
            # if length of current is 2n, stop recursing
            if len(current) == 2 * n:
                result.append(current)
                return

            # add open is count is less than n
            if n_open < n:
                recur(current + '(', n_open+1, n_close)
            # only add close when there is more opened than closed
            if n_close < n_open:
                recur(current + ')', n_open, n_close+1)

        recur()
        return result


s = Solution()
assert s.generateParenthesis(0) == ['']
assert s.generateParenthesis(1) == ['()']
assert s.generateParenthesis(2) == ["(())", "()()"]
assert s.generateParenthesis(3) == [
    "((()))", "(()())", "(())()", "()(())", "()()()"
]
assert s.generateParenthesis(4) == [
    "(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
    "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"
]
assert s.generateParenthesis2(0) == ['']
assert s.generateParenthesis2(1) == ['()']
assert s.generateParenthesis2(2) == ["(())", "()()"]
assert s.generateParenthesis2(3) == [
    "((()))", "(()())", "(())()", "()(())", "()()()"
]
assert s.generateParenthesis2(4) == [
    "(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
    "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"
]
