# https://leetcode.com/problems/valid-parentheses/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# original


def isValid(self, s: str) -> bool:
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    stack = []
    for ch in s:
        is_opening = ch in opening
        last_opened = stack[-1] if len(stack) > 0 else None

        if is_opening:
            stack.append(ch)
        elif last_opened and closing.index(ch) == opening.index(last_opened):
            stack.pop()
        else:
            return False

    return len(stack) == 0

# alternate, improved?


def isValid2(self, s: str) -> bool:
    stack = []

    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.append(ch)
        else:
            if not stack or stack.pop() + ch not in {'()', '[]', '{}'}:
                return False

    return not stack


valid_pairs = '()[]{}||'


def parseString(string):
    result = ''
    for ch in string:
        if ch in valid_pairs:
            result += ch
    return result


def balanced_brackets(string):
    stack = []
    open_pipe = False

    for ch in parseString(string):
        if ch in '[({|' and not open_pipe:
            stack.append(ch)
            if ch == '|':
                open_pipe = not open_pipe
        else:
            if len(stack) == 0 or stack.pop() + ch not in valid_pairs:
                return False
            if ch == '|':
                open_pipe = not open_pipe

    return len(stack) == 0 or not open_pipe


print(balanced_brackets("([)]"))  # false
print(balanced_brackets("(foo[barr]||)"))  # true
