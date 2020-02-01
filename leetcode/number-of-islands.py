# https://leetcode.com/problems/number-of-islands/
'''
Islands are contiguous regions of 1s in a sea of 0s. Assume edges are water (0s).
Iterate over grid, if not visited and is not 0, increment island count and search of all connected ones so they will be added to visited. Could also modify the input to mark location as visited to memory usage.
Return island count. 
'''
from typing import List


class Solution:
    def iterate_matrix(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                yield r, c

    def is_in_bounds(self, grid, row, col):
        return all((row >= 0, row < len(grid), col >= 0, col < len(grid[0])))

    def iterate_adjacent_cells(self, grid, row, col):
        for dR, dC in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            i = row + dR
            j = col + dC
            if self.is_in_bounds(grid, i, j):
                yield (i, j)

    def count_regions(self, grid, row, col, target, visited):
        # are we in the sea, or have we been here before?
        if grid[row][col] != target or (row, col) in visited:
            return 0

        # first cell in a connected region
        visited.add((row, col))
        # visit all connected cells and mark visited
        for i, j in self.iterate_adjacent_cells(grid, row, col):
            self.count_regions(grid, i, j, target, visited)
        # new region found
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        islands = 0
        visited = set()
        for r, c in self.iterate_matrix(grid):
            islands += self.count_regions(grid, r, c, '1', visited)

        return islands


s = Solution()
one = [["1", "1", "1", "1", "0"],
       ["1", "1", "0", "1", "0"],
       ["1", "1", "0", "0", "0"],
       ["0", "0", "0", "0", "0"]]
three = [["1", "1", "0", "0", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "0", "0", "1", "1"]]
assert s.numIslands(one) == 1
assert s.numIslands(three) == 3
