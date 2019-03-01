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


def isUniqueInRowAndCol(value, values):
    for v in values:
        # don't compare case with itself
        if v == value:
            continue
        if (v['row'] == value['row'] or v['col'] == value['col']) and v['value'] == value['value']:
            return False

    return True


def translateCoordToSubGrid(value):
    x = math.floor(value['row'] / 3)
    y = math.floor(value['col'] / 3)
    return x, y


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
        x, y = translateCoordToSubGrid(v)
        subGrid[x][y].append(v)

    for row in subGrid:
        for location in row:
            for value in location:
                for v in location:
                    if v == value:
                        continue
                    if (v['value'] == value['value']):
                        return False

    return True


def sudoku2(grid):

    values = []
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value in '0123456789':
                values.append({'value': value, 'row': x, 'col': y})

    if not areUniqueInNinths(values):
        return False

    for value in values:
        if not isUniqueInRowAndCol(value, values):
            return False

    return True


print("Test 1 passes:", sudoku2(gridFalse) == False)
print("Test 2 passes:", sudoku2(gridTrue) == True)
