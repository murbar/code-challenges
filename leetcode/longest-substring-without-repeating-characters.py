# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return len(s)

        max_length = 1
        current_length = 1
        # store the chars we've seen with their index
        current_chars = {s[0]: 0}
        i = 1
        while i < len(s):
            char = s[i]
            if char in current_chars:
                # char is a repeat, start again just after the last time this char appeared
                # set max length
                max_length = max(max_length, current_length)
                # reset current substring length
                current_length = 0
                # move pointer to char after where this char first appeared
                i = current_chars[char] + 1
                # reset the chars seen
                current_chars.clear()
            else:
                # we haven't seen this char yet
                # increment length of current substring
                current_length += 1
                # add to chars seen with index
                current_chars[char] = i
                # move pointer to next position in string
                i += 1

        # current length may be larger than max_length if it is at the end of the
        # input string, ie. we haven't set max_length because no char has repeated
        return max(max_length, current_length)

    def lengthOfLongestSubstring2(self, s):
        # much faster we only iterate over each char once, O(n) time, O(m) space
        # keep setting indexes in seen dict as we go, no need to reset dict
        seen = {}
        max_so_far = 0
        current_max = 0
        substring_start = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= substring_start:
                max_so_far = max(max_so_far, current_max)
                current_max = i - seen[char]
                substring_start = seen[char] + 1
            else:
                current_max += 1

            seen[char] = i

        return max(max_so_far, current_max)
