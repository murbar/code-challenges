# https://leetcode.com/problems/word-break-ii/

from typing import List


class Solution:
    # much too slow for large inputs
    def search(self, s, out, dictionary, results):
        if len(s) == 0:
            # remove the leading space
            results.append(out[1:])
            return

        for i in range(1, len(s)+1):
            prefix = s[:i]
            if prefix in dictionary:
                self.search(s[i:], f'{out} {prefix}', dictionary, results)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictionary = set(wordDict)
        results = []
        self.search(s, '', dictionary, results)
        return results


class SolutionDP:

    def check(self, string, dictionary):
        length = len(string)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(length):
            for j in range(i, length+1):
                if dp[i] and string[i:j] in dictionary:
                    dp[j] = True

        return dp

    def search(self, string, path, dp, i, dictionary, result):
        if dp[i+len(string)]:
            if not string:
                # remove the leading space
                result.append(path.strip())

            for j in range(1, len(string)+1):
                prefix = string[:j]
                if prefix in dictionary:
                    self.search(
                        string[j:], f'{path} {prefix}', dp, i+j, dictionary, result)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return ['']

        dictionary = set(wordDict)
        dp = self.check(s, dictionary)
        result = []
        self.search(s, '', dp, 0, dictionary, result)
        return result


s = Solution()
dp = SolutionDP()
test_cases = [
    (('leetcode', ['leet', 'code']), ['leet code']),
    (('pineapplepenapple', ['apple', 'pen',
                            'applepen', 'pine', 'pineapple']), [
        'pine apple pen apple',
        'pineapple pen apple',
        'pine applepen apple'
    ]),
    (('aaaaaaa', ['aaaa', 'aaa']), [
        'aaaa aaa',
        'aaa aaaa'
    ]),
    (('catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']), [
        'cats and dog',
        'cat sand dog'
    ]),
    (('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']), []),
    (('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
       aaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaa\
       aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', [
     'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa',
        'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']), [])
]


def run_tests(func, cases):
    failures = 0
    for case in cases:
        args, expected = case
        result = func(*args)
        try:
            assert sorted(result) == sorted(expected)
        except AssertionError:
            failures += 1
            print(f'FAILED {func.__self__.__class__.__name__}')
            print(f'Input: {args}')
            print(f'Returned: {result}, Expected: {expected}')

    if not failures:
        print('All tests passed')


run_tests(dp.wordBreak, test_cases)
