# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn

# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

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


def sudoku2(grid):
    # grid is len(grid) x len(grid[0]) in size
    # for each element in grid
    #   get coords (x, y)
    #
    #
    #
    #
    #
    #
    #
    #
