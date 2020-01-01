# https://www.hackerrank.com/challenges/ctci-ransom-note/


def get_counts(word_list):
    counts = {}
    for w in word_list:
        counts[w] = counts.get(w, 0) + 1
    return counts


def checkMagazine(magazine, note):
    m = get_counts(magazine)
    n = get_counts(note)

    for word, count in n.items():
        if count > m.get(word, 0):
            return "No"

    return "Yes"


# if __name__ == '__main__':
#     mn = input().split()
#     m = int(mn[0])
#     n = int(mn[1])
#     magazine = input().rstrip().split()
#     note = input().rstrip().split()
#     print(checkMagazine(magazine, note))
