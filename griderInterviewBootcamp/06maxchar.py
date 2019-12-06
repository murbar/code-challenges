# variations: most common character in a string, are two strings anagrams, does given string have repeated chars
from collections import Counter

#  for anagrams, compare two count dicts and see if all keys are equal


def max_char(string):
    counts = {}
    m = 0
    char = ''

    for ch in string:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1

    for ch, c in counts.items():
        if c > m:
            m = c
            char = ch

    return char


def max_char2(string):
    counts = Counter(string)
    return counts.most_common(1)[0][0]


assert max_char('abccccccccd') == 'c'
assert max_char2('abccccccccd') == 'c'
print('All tests passed!')
