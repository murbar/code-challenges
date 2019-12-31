# https://leetcode.com/problems/longest-palindromic-substring/


def longestPalindrome(s: str) -> str:
    # solution doesn't quite work
    result = ''

    for i in range(len(s)):
        pal = s[i]
        start, end = i-1, i+1
        while start > 0 and end < len(s):
            print(i)
            if s[start] == s[end]:
                pal = s[start:end+1]
                start -= 1
                end += 1
            elif s[start] == s[i]:
                pal = s[start:i+1]
                start -= 1
                print(pal, start, end)
                # end = i
            elif s[end] == s[i]:
                pal = s[i:end+1]
                # start = i
                end += 1
            else:
                print(start, end, i)
                break

        if len(pal) > len(result):
            result = pal

    return result


# found solution below
# https://leetcode.com/articles/longest-palindromic-substring/


def expand_on_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1  # note subtract 1


def longestPalindrome2(s: str) -> str:
    if not s:
        return ''

    start, end = 0, 0
    for i in range(len(s)):
        # handle candidate palindromes with even and odd lengths
        l1 = expand_on_center(s, i, i)
        l2 = expand_on_center(s, i, i+1)
        max_len = max(l1, l2)
        if max_len > end - start:
            # note integer division
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end+1]


# assert longestPalindrome("cbbd") == "bb"
# assert longestPalindrome("babad") == "aba"
# assert longestPalindrome("babadtcbbctcbbt") == "tcbbct"
assert longestPalindrome2("cbbd") == "bb"
assert longestPalindrome2("babad") == "aba"
assert longestPalindrome2("babadtcbbctcbbt") == "bbctcbb"
assert longestPalindrome2("bb") == "bb"
assert longestPalindrome2("") == ""
# print(longestPalindrome2("babadtcbbctcbbt"))
# print(longestPalindrome('tcabbact'))
# print(longestPalindrome('bb'))
