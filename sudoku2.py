# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn

# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a
# way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all
# contain all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid
# Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by
# grid does not have to be solvable.

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
# list of nine empty lists
#   if row 0-2,
# compare values of each case in subgrid


def isUniqueInRow(case, cases):
    for c in cases:
        if c == case:
            continue
        # combine these in future with logical or and ()
        if c['row'] == case['row'] and c['value'] == case['value']:
            print('X FAIL', c, case)
            return False

    return True


def isUniqueInCol(case, cases):
    for c in cases:
        if c == case:
            continue
        if c['col'] == case['col'] and c['value'] == case['value']:
            print('Y FAIL', c, case)
            return False

    return True


def isUniqueInNinth(case, cases):
    return True


def isValid(case, cases, grid):
    return isUniqueInRow(case, cases) and \
        isUniqueInCol(case, cases) and \
        isUniqueInNinth(case, cases)


def sudoku2(grid):
    cases = []

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value in '0123456789':
                cases.append({'row': x, 'col': y, 'value': value})

    print(cases)
    for case in cases:
        if not isValid(case, cases, grid):
            return False

    return True


print(sudoku2(gridFalse))
# print([(x, y) for (x, y) in enumerate(gridFalse)])
