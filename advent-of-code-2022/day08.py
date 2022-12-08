from utils import read_text_file

forest = read_text_file('day08input.txt').splitlines()

# for each element in the grid
# if element is on the edge, count visible
# else check if element is visible from left, top, right, bottom
# return visible count
# how could we make this more efficient
#   keep track of tallest so far in row/col?


def is_first_or_last(ls, i):
    return i == 0 or i == (len(ls) - 1)


def get_items_on_both_sides(string, i):
    ls = [*string]
    before = ls[:i]
    after = ls[i+1:]
    return [int(t) for t in before], [int(t) for t in after]


def get_max_both_sides(trees, i):
    before, after = get_items_on_both_sides(trees, i)
    return max(before), max(after)


def is_visible(row, col, i, j):
    height = int(row[j])
    # careful with i and j here, we want to split on the col # in the row
    # and the row # in the col
    max_left, max_right = get_max_both_sides(row, j)
    max_top, max_bottom = get_max_both_sides(col, i)
    if any((True for m in [max_right, max_left, max_top, max_bottom] if height > m)):
        return True
    return False


def count_trees_visible(height, sight_line):
    visibility = 1
    for tree in sight_line:
        if height > tree:
            visibility += 1
        else:
            break
    # if all trees in line are shorter, we'll be off by one when we reach the end of the line
    return min(visibility, len(sight_line))


def get_visibility_score(row, col, i, j):
    height = int(row[j])
    to_left, to_right = get_items_on_both_sides(row, j)
    to_top, to_bottom = get_items_on_both_sides(col, i)
    l = count_trees_visible(height, [*reversed(to_left)])
    r = count_trees_visible(height, to_right)
    t = count_trees_visible(height, [*reversed(to_top)])
    b = count_trees_visible(height, to_bottom)
    return l * r * t * b


def get_col(grid, j):
    return ''.join([row[j] for row in grid])


def count_visible_trees(forest):
    visible_count = 0
    max_visibilty = 0  # i, j, score

    for i, row in enumerate(forest):
        for j, _ in enumerate(row):
            col = get_col(forest, j)
            if is_first_or_last(row, i) or is_first_or_last(col, j):
                visible_count += 1
            else:
                if is_visible(row, col, i, j):
                    visible_count += 1

                score = get_visibility_score(row, col, i, j)
                if score > max_visibilty:
                    max_visibilty = score

    return visible_count, max_visibilty


solution_A, solution_B = count_visible_trees(forest)
print("A:", solution_A)
print("B:", solution_B)
