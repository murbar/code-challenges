def extract_nums(line):
    return [x for x in line if x in '0123456789']


def check_unique(line):
    nums = extract_nums(line)
    return len(set(nums)) == len(nums)


def rows_valid(grid):
    return all([check_unique(row) for row in grid])


def cols_valid(grid):
    n_grid_rows = range(len(grid))
    return all([check_unique([row[i] for row in grid]) for i in n_grid_rows])


def subgrids_valid(grid):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False

    return True


def sudoku2(grid):
    return rows_valid(grid) and cols_valid(grid) and subgrids_valid(grid)
