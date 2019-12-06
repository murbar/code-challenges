# ignore whitespace and punctuation
import re


def anagrams(stringA, stringB):
    # O(2n log n + 2m log m)
    charsA = [ch.lower() for ch in stringA if ch.isalpha()]
    charsB = [ch.lower() for ch in stringB if ch.isalpha()]
    return sorted(charsA) == sorted(charsB)


def anagrams2(stringA, stringB):
    # O(2n + m)
    def count_chars(string):
        counts = {}
        for ch in string:
            ch = ch.lower()
            if ch.isalpha():
                counts.setdefault(ch, 0)
                counts[ch] = counts[ch] + 1
        return counts

    countsA = count_chars(stringA)
    countsB = count_chars(stringB)

    if len(countsA) != len(countsB):
        return False

    for k, v in countsA.items():
        if v != countsB[k]:
            return False

    return True


assert anagrams('rail safety', 'fairy tales')
assert anagrams('RAIL! SAFETY!', 'fairy tales')
assert not anagrams('Hi there', 'Bye there')
assert anagrams2('rail safety', 'fairy tales')
assert anagrams2('RAIL! SAFETY!', 'fairy tales')
assert not anagrams2('Hi there', 'Bye there')
print('All tests passed!')
