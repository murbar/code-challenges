import re
from utils import read_text_file

stacks_raw, moves_raw = read_text_file('day05input.txt').split("\n\n")


def get_ints(string):
    return [int(x) for x in re.findall(r'\d+', string)]


def get_caps(string):
    return [x for x in re.findall(r'[A-Z]', string)]


def filter_for_caps(ls):
    filtered = []
    for x in ls:
        item = get_caps(x)
        if item:
            filtered.append(item[0])
    return filtered


def split_every(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]


def parse_matrix(text):
    lines = text.split("\n")
    return [split_every(line, 4) for line in lines]


def rotate_matrix(matrix):
    return [list(x) for x in zip(*matrix[::-1])]


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


def move_items_one_by_one(stacks, instruction):
    count, src, dest = instruction
    for _ in range(count):
        stacks[dest-1].append(stacks[src-1].pop())


def move_items_all_at_once(stacks, instruction):
    count, src, dest = instruction
    stacks[dest-1].extend(stacks[src-1][-count:])
    stacks[src-1] = stacks[src-1][:-count]


def get_last(stacks):
    return "".join([stack[-1] for stack in stacks])


def solveA(moves):
    matrix = parse_matrix(stacks_raw)
    rotated = rotate_matrix(matrix)
    stacks = [filter_for_caps(s) for s in rotated]
    for m in moves:
        move_items_one_by_one(stacks, m)
    return get_last(stacks)


def solveB(moves):
    matrix = parse_matrix(stacks_raw)
    rotated = rotate_matrix(matrix)
    stacks = [filter_for_caps(s) for s in rotated]
    for m in moves:
        move_items_all_at_once(stacks, m)
    return get_last(stacks)


moves = [get_ints(m) for m in moves_raw.split("\n")]  # count, from, to
print(solveA(moves))
print(solveB(moves))
