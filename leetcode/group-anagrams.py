# https://leetcode.com/problems/group-anagrams/

# first thought is to sort each word, compare anagrams, and save indexes of matches to a dictionary

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(nk lg n) time, O(nk) space, n = number of words, k = length of longest word
        indexes = {}

        for word in strs:
            key = tuple(sorted(word))
            indexes[key] = [*indexes.get(key, []), word]

        return list(indexes.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # a bit more performant IF words are relatively large
        # (in theory at least, sorting seems to benchmark at twice the speed of count for any length word...)
        # count the occurrence of characters in lieu of sorting
        # O(nk) time and space, n = number of words, k = length of longest word
        indexes = {}

        for word in strs:
            # key char counts
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            key = ''.join(str(c) for c in counts)
            indexes[key] = [*indexes.get(key, []), word]

        return list(indexes.values())
