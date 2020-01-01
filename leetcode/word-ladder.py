# https://leetcode.com/problems/word-ladder/

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# recognize this is a graph problem
# comes from practice and intuition
# problem statement mentions "sequence", "relationships"
# often get graphs problems in interview setting,
# STEPS TO SOLVE(almost) ANY GRAPHS PROBLEM!
# * Translate the problem into graph terminology
# * Build your graph
# * Traverse your graph

# Looking for shortest path - indicates BFS
# Looking for sequence - need the BFS path
# word -> vertex
# one letter change -> edge

# 1. implement traversal
# 2. get neighbors


from collections import defaultdict


class Solution:
    def get_neighbors(self, word, word_list):
        neighbors = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        word_chars = list(word)

        for i in range(len(word_chars)):
            for l in letters:
                chars = word_chars.copy()
                chars[i] = l
                candidate = "".join(chars)

                if candidate != word and candidate in word_list:
                    neighbors.append(candidate)

        return neighbors

    def ladderLength(self, begin_word, end_word, word_list):
        word_set = set(word_list)
        visited = set()
        sequence_queue = []
        sequence_queue.append([begin_word])

        while sequence_queue:
            sequence = sequence_queue.pop(0)
            word = sequence[-1]

            if word not in visited:
                visited.add(word)

                if word == end_word:
                    return len(sequence)
                for n in self.get_neighbors(word, word_set):
                    s = sequence.copy()
                    s.append(n)
                    sequence_queue.append(s)

        return 0


# leetcode solution
# build adjacency list with intermediate words
class Solution2:
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        word_len = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord}
        while queue:
            current_word, level = queue.popleft()
            for i in range(word_len):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
