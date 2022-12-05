from utils import read_text_file

pairs = read_text_file('day04input.txt').split("\n")


def get_range(string):
    i, j = string.split('-')
    return int(i), int(j)


def split_pair(string):
    a, b = string.split(',')
    return get_range(a), get_range(b)


def is_subset(i, j):
    return i[0] >= j[0] and i[1] <= j[1]


def has_overlap(a, b):
    i, j = a
    k, l = b
    for x in range(i, j+1):
        if x in range(k, l+1):
            return True
    return False


def check_pairs_for_subsets(pairs):
    subsets = 0
    for pair in pairs:
        a, b = split_pair(pair)
        if is_subset(a, b) or is_subset(b, a):
            subsets += 1
    return subsets


def check_pairs_for_overlaps(pairs):
    overlaps = 0
    for pair in pairs:
        if has_overlap(*split_pair(pair)):
            overlaps += 1
    return overlaps


print("subsets", check_pairs_for_subsets(pairs))
print("overlaps", check_pairs_for_overlaps(pairs))
