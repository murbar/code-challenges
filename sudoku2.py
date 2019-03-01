# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn

# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a
# way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all
# contain all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid
# Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by
# grid does not have to be solvable.

import math

gridTrue = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

gridFalse = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
             ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
             ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
             ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
             ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
             ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
             ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
             ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

# The given grid is not correct because there are two 1s in the second column. Each column, each
# row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

# pseudocode
# grid is len(grid) x len(grid[0]) in size
# for each element in grid
#   get coords (x, y)
#   determine sector (1-9)
#   for each row in grid
#       check row[x] for element
#       return true if unique
#   for each element in grid[y]
#       check element
#
#
#

# for each case
#   compare to all cases with same x
#       return False is value of el match
#   compare to all cases with same y
#       return False if value of el match

# subgrid
# sort cases in to 9 possible subgrids
# (list of nine empty lists?)
#   if case row 0-2 and col 0-2 -> ninths[0].append(el)
#   etc, etc
# for n in ninths
#   if len(n) > 1
#       compare els in n, return False is values are equal
#
# compare values of each case in subgrid


def isUniqueInRowAndCol(value, values):
    for v in values:
        # don't compare case with itself
        if v == value:
            continue
        if (v['row'] == value['row'] or v['col'] == value['col']) and v['value'] == value['value']:
            print('INVALID', v, value)
            return False

    return True


def translateCoord(value):
    x = math.floor(value['row'] / 3)
    y = math.floor(value['col'] / 3)
    return x, y


# def isUniqueInNinth(value, values):
#     print((values))
#     # init 3 x 3 grid
#     subGrid = [[[]] * 3] * 3
#     for v in values:
#         print(v)
#         x, y = translateCoord(v)
#         subGrid[x][y].append('•')
#     print(subGrid)
#     return True


def areUniqueInNinths(values):
    # init 3 x 3 grid
    # WHOOPS this creates referenced copies such that mutating one list mutates all nine!
    # amateur hour ↓
    # subGrid = [[[]] * 3] * 3
    # solution ↓
    subGrid = [[[], [], []],
               [[], [], []],
               [[], [], []]]

    for v in values:
        x, y = translateCoord(v)
        subGrid[x][y].append(v)

    for row in subGrid:
        for location in row:
            for value in location:
                for v in location:
                    if v == value:
                        continue
                    if (v['value'] == value['value']):
                        print('INVALID', v, value)
                        return False

    return True


def isValid(value, values):
    return isUniqueInRowAndCol(value, values) and isUniqueInNinth(value, values)


def sudoku2(grid):

    values = []
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value in '0123456789':
                values.append({'value': value, 'row': x, 'col': y})

    # for value in values:
    #     if not isValid(value, values):
    #         return False

    areUniqueInNinths(values)

    return True


print(sudoku2(gridFalse))
# print([(x, y) for (x, y) in enumerate(gridFalse)])
