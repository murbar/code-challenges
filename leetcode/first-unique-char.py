# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i

        return -1
