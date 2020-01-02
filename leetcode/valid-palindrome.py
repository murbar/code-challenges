# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]

        if not len(chars):
            return True

        i, j = 0, len(chars) - 1
        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1

        return True
