# https://leetcode.com/problems/unique-paths/

# count unique paths from top-right to bottom-right on a grid
# can only move down or right
# graph traversal... dynamic programming?
# could have an memo dict to store number of unique paths at each location, use them to
# calculate adjacent values


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(mn) time and space
        if not m or not n:
            return 1

        # cannot move up or right, so only one way to get to each location in the top row
        # and left column
        # beware [[-1] * m] * n - creates a list of n references to the same list
        grid = [[1] * m for _ in range(n)]

        for row in range(1, n):
            for col in range(1, m):
                # ways to here is the sum of the ways of the locations above and to the right
                grid[row][col] = grid[row-1][col] + grid[row][col-1]

        # return ways to last col in last row
        return grid[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        # reduce space complexity to n by only storing the last computed row
        if not m or not n:
            return 1

        last_row = [1] * m
        for _ in range(1, n):
            for col in range(1, m):
                last_row[col] += last_row[col-1]

        return last_row[-1]


s = Solution()
assert s.uniquePaths(7, 3) == 28
assert s.uniquePaths(3, 2) == 3
assert s.uniquePaths(1, 1) == 1
assert s.uniquePaths(1, 0) == 1
assert s.uniquePaths(0, 1) == 1
assert s.uniquePaths(0, 0) == 1
assert s.uniquePaths(15, 15) == 40116600

assert s.uniquePaths2(7, 3) == 28
assert s.uniquePaths2(3, 2) == 3
assert s.uniquePaths2(1, 1) == 1
assert s.uniquePaths2(1, 0) == 1
assert s.uniquePaths2(0, 1) == 1
assert s.uniquePaths2(0, 0) == 1
assert s.uniquePaths2(15, 15) == 40116600
