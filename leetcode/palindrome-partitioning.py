# https://leetcode.com/problems/palindrome-partitioning/

# brute force: generate all possible decompositions and check if each is a palindrome
# lot's of wasted work
# solution: backtracking


from typing import List


# solution 1


def is_palindrome(word: str) -> bool:
    if not len(word):
        return False

    return word == word[::-1]


def decompose(s: str, p: int, in_progress: List, results: List) -> None:
    if p == len(s):
        results.append(in_progress.copy())
    else:
        for i in range(p, len(s)+1):
            snippet = s[p:i]
            if is_palindrome(snippet):
                in_progress.append(snippet)
                decompose(s, i, in_progress, results)
                in_progress.pop()


class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        decompositions = []
        decompose(s, 0, [], decompositions)
        return decompositions


# solution 2
# less space efficient since we're copying the string on each recursive call

def dfs(s, path, results):
    if not s:
        results.append(path.copy())
    else:
        for i in range(1, len(s)+1):
            snippet = s[:i]
            if is_palindrome(snippet):
                path.append(snippet)
                dfs(s[i:], path, results)
                path.pop()


class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        decompositions = []
        dfs(s, [], decompositions)
        return decompositions


# solution 3: dynamic programming


class Solution3:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[[]]]
        psi = [1]   # palindrome start indices
        for i, c in enumerate(s):
            next_pp = []
            next_psi = [i+1, i+2]
            for k in psi:
                if k >= 1 and s[k-1] == s[i]:
                    next_psi.append(k-1)
                    for pp in dp[k-1]:
                        next_pp.append(pp + [s[k-1:i+1]])
            psi = next_psi
            dp.append(next_pp)
        return dp[-1]


s1 = Solution1()
s2 = Solution2()
s3 = Solution3()

assert s1.partition('aab') == [['a', 'a', 'b'], ['aa', 'b']]
assert s2.partition('aab') == [['a', 'a', 'b'], ['aa', 'b']]
assert s3.partition('aab') == [['aa', 'b'], ['a', 'a', 'b']]
