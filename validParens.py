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
