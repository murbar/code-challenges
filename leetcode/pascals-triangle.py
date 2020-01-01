# https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        # first row
        triangle = [[1]]
        # for any row following first
        for row_i in range(1, numRows):
            preceding = triangle[-1]
            # length of row is i + 1
            row = [1] * (row_i + 1)

            # skip first and last element
            for i in range(1, row_i):
                row[i] = preceding[i-1] + preceding[i]

            triangle.append(row)

        return triangle


# https://leetcode.com/problems/pascals-triangle-ii/
# return only the row at given index
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # first row, index 0
        last_row = [1]
        # for any row with index > 0
        for row_i in range(1, rowIndex+1):
            # length of row is i + 1
            row = [1] * (row_i + 1)

            # skip first and last element
            for i in range(1, row_i):
                row[i] = last_row[i-1] + last_row[i]

            last_row = row

        return last_row
