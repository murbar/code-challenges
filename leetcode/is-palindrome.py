# https://leetcode.com/problems/valid-palindrome/

# problem seems to be broken on leetcode


def isPalindrome(s):
    chars = [c.lower() for c in s if c.isalpha()]

    if not len(chars):
        return True

    i, j = 0, len(chars) - 1
    while i < j:
        if chars[i] != chars[j]:
            return False
        i += 1
        j -= 1

    return True


assert isPalindrome("A man, a plan, a canal: Panama")
assert isPalindrome("")
assert not isPalindrome("race a car")
