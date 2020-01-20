# https://leetcode.com/problems/valid-palindrome/

# problem seems to be broken on leetcode
# edge case: is an empty string a palindrome?


def is_palindrome(s):
    chars = [c.lower() for c in s if c.isalpha()]

    i, j = 0, len(chars) - 1
    while i < j:
        if chars[i] != chars[j]:
            return False
        i += 1
        j -= 1

    return True


def is_palindrome2(s):
    chars = [c.lower() for c in s if c.isalpha()]
    return all(chars[i] == chars[~i] for i in range(len(chars) // 2))


assert not is_palindrome('asdf')
assert not is_palindrome('abaa')
assert not is_palindrome('abbaa')
assert not is_palindrome('ab')
assert is_palindrome('aa')
assert is_palindrome('a')
assert is_palindrome('')
assert is_palindrome('aca')
assert is_palindrome('aabbaa')
assert is_palindrome('aabcbaa')
assert is_palindrome("A man, a plan, a canal: Panama")
assert is_palindrome("")
assert not is_palindrome("race a car")

assert not is_palindrome2('asdf')
assert not is_palindrome2('abaa')
assert not is_palindrome2('abbaa')
assert not is_palindrome2('ab')
assert is_palindrome2('aa')
assert is_palindrome2('a')
assert is_palindrome2('')
assert is_palindrome2('aca')
assert is_palindrome2('aabbaa')
assert is_palindrome2('aabcbaa')
assert is_palindrome2("A man, a plan, a canal: Panama")
assert is_palindrome2("")
assert not is_palindrome2("race a car")
