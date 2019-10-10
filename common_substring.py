# https://www.hackerrank.com/challenges/two-strings

ALPHABET_SIZE = 26


def get_index(ch):
    return ord(ch) - ord('a')


def twoStringsWithVector(s1, s2):
    vector = [0] * ALPHABET_SIZE

    for ch in s1:
        vector[get_index(ch)] = True

    for ch in s2:
        if vector[get_index(ch)]:
            return 'YES'

    return 'NO'


def twoStringsWithDict(s1, s2):
    chars = {}

    for ch in s1:
        chars[ch] = True

    for ch in s2:
        if chars.get(ch, False):
            return 'YES'

    return 'NO'


def twoStringsWithSet(s1, s2):
    chars = set(list(s1))

    for ch in s2:
        if ch in chars:
            return 'YES'

    return 'NO'


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     q = int(input())

#     for q_itr in range(q):
#         s1 = input()
#         s2 = input()
#         result = twoStrings(s1, s2)
#         fptr.write(result + '\n')

#     fptr.close()
