# https://leetcode.com/problems/word-break/


'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
- words can be used more than once
- no dupes in the word list
- recursion, dynamic programming
    - optimal substructure, can be broken into ever smaller problems
    - overlapping subproblems, same subproblem will be solved more than once
        - illustrated by drawing the recursion tree
    - memoize subproblem solutions rather than compute them again
- use trie data structure to optimize performance
- https://www.youtube.com/watch?v=hLQYQ4zj0qg
'''

from typing import List


class SolutionRecursive:
    # recursive, top down, memoization

    def search(self, word, start, dictionary, memo):
        # this solution is impractical for large inputs
        # unless we memoize intermediate results
        if start == len(word):
            return True

        if start in memo:
            return memo[start]

        for i in range(start, len(word)):
            target = word[start:i+1]
            if target in dictionary and self.search(word, i+1, dictionary, memo):
                memo[start] = True
                return True

        memo[start] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        memo = {}
        result = self.search(s, 0, dictionary, memo)
        return result


class SolutionDP:
    # bottom-up, dynamic programming
    # about 2x faster than recursive
    # O(n^2) time, O(n) space, where n is the length of input string

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        # dp[i] True if first i chars of word can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]


# using a trie
class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        # does this node complete a full word?
        self.terminal = False


def insert_trie(head, word):
    node = head

    for ch in word:
        if not node.children.get(ch, None):
            node.children[ch] = TrieNode(ch)
        node = node.children[ch]
    # last ch completes a word
    node.terminal = True


class SolutionTrie:
    # more complex solution, better performance
    # about 25x faster than DP
    # O(w) time, where w is length of longest word in dictionary (height of the trie)
    # O(n+m) space, where n is the size of the input string and m is the sum of the lengths of
    # all the words in the dictionary

    def search(self, head, word):
        # dp[i] True if first i chars of word can be segmented
        dp = [False] * (len(word) + 1)
        dp[0] = True

        for i in range(len(word)):
            # loop until segmentation is impossible
            if dp[i]:
                node = head
                for j in range(i, len(word)):
                    if node is None:
                        break

                    node = node.children.get(word[j], None)
                    if node is not None and node.terminal:
                        dp[j+1] = True

        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = TrieNode()
        for w in wordDict:
            insert_trie(trie, w)

        return self.search(trie, s)


rec = SolutionRecursive()
dp = SolutionDP()
tr = SolutionTrie()
test_cases = [
    (('leetcode', ['leet', 'code']), True),
    (('applepenapple', ['apple', 'pen']), True),
    (('aaaaaaa', ['aaaa', 'aaa']), True),
    (('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']), False),
    (('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
        aaaaaaaaaaaaaaaaaaaaaaaaab',
      ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa',
       'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']), False)
]


def run_tests(funcs, cases):
    failures = 0
    for f in funcs:
        for case in cases:
            args, expected = case
            result = f(*args)
            try:
                assert result == expected
            except AssertionError:
                failures += 1
                print(f'FAILED {f.__self__.__class__.__name__}')
                print(f'Input: {args}')
                print(f'Returned: {result}, Expected: {expected}')

    if not failures:
        print('All tests passed')


run_tests([rec.wordBreak, dp.wordBreak, tr.wordBreak], test_cases)
