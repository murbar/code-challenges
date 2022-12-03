from utils import read_text_file

# Part A
# split string in half
# determine which character exists in both halves
# score the character

sacks = read_text_file('day03input.txt').split("\n")


def split_string(string):
    half = len(string) // 2
    return string[:half], string[half:]


def find_common_char_in_list(strings):
    for char in strings[0]:
        if all(char in string for string in strings):
            return char
    return None


def score_char(char):
    code = ord(char) - 96
    if code < 0:
        return code + 58
    return code


def solveA():
    solutionA = 0
    for sack in sacks:
        half1, half2 = split_string(sack)
        common_char = find_common_char_in_list([half1, half2])
        solutionA += score_char(common_char)
    return solutionA


print("solution A", solveA())

# Part B
# group list items in groups of 3 items
# determine which character exists in all 3 items
# score the character


def group_list_items(items, group_size=3):
    group = []
    for item in items:
        group.append(item)
        if len(group) == group_size:
            yield group
            group = []


def solveB():
    solutionB = 0
    for group in group_list_items(sacks):
        common_char = find_common_char_in_list(group)
        solutionB += score_char(common_char)
    return solutionB


print("solution B", solveB())


