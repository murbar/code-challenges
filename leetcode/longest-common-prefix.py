# https://leetcode.com/problems/longest-common-prefix/


def every(ls, test):
    for i in ls:
        if not test(i):
            return False

    return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        i = 0
        while True:
            prefix = strs[0][:i]
            last_prefix = strs[0][:i-1]
            if i > 0 and prefix == last_prefix:
                break
            if every(strs, lambda s: s[:i] == prefix):
                i += 1
            else:
                break

        return strs[0][:i-1]
