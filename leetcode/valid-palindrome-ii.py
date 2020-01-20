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


# https://leetcode.com/problems/valid-palindrome-ii/
# is it a palindrome with any one letter removed?
class Solution2:
    def validPalindrome(self, s: str) -> bool:

        def helper(word, error=False):
            if not len(word):
                return True

            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    if error:
                        return False
                    else:
                        without_i = s[:i] + s[i+1:]
                        without_j = s[:j] + s[j+1:]
                        return helper(without_i, True) or helper(without_j, True)
                i += 1
                j -= 1

            return True

        return helper(s)

    # not my solution
    def validPalindrome2(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        for i in range(len(s) / 2):
            # ~1 == -(i+1)
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)
        return True
