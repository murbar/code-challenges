from utils import read_text_file

buffer = read_text_file('day06input.txt')


def all_chars_unique(string):
    return len(set(string)) == len(string)


def find_starting_index(buffer, size):
    for i in range(len(buffer)-size):
        j = i + size
        if all_chars_unique(buffer[i:j]):
            return j


def solve_a():
    return find_starting_index(buffer, 4)


def solve_b():
    return find_starting_index(buffer, 14)


solution_a = solve_a()
solution_b = solve_b()
print(solution_a)
print(solution_b)
