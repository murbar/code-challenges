# ignore whitespace and punctuation
import re


def anagrams(stringA, stringB):
    # O(2n log n + 2m log m)
    charsA = [ch.lower() for ch in stringA if ch.isalpha()]
    charsB = [ch.lower() for ch in stringB if ch.isalpha()]
    return sorted(charsA) == sorted(charsB)


def anagrams2(stringA, stringB):
    # O(2n + m)
    stringA = ''.join([ch.lower() for ch in stringA if ch.isalpha()])
    stringB = ''.join([ch.lower() for ch in stringB if ch.isalpha()])

    if len(stringA) != len(stringB):
        return False

    counts = {}
    for i in range(len(stringA)):
        a, b = stringA[i], stringB[i]
        if a.isalpha():
            counts[a] = counts.get(a, 0) + 1
        if b.isalpha():
            counts[b] = counts.get(b, 0) - 1

    for c in counts.values():
        if c != 0:
            return False

    return True


assert anagrams('rail safety', 'fairy tales')
assert anagrams('RAIL! SAFETY!', 'fairy tales')
assert not anagrams('Hi there', 'Bye there')
assert anagrams2('rail safety', 'fairy tales')
assert anagrams2('RAIL! SAFETY!', 'fairy tales')
assert not anagrams2('Hi there', 'Bye there')
print('All tests passed!')
