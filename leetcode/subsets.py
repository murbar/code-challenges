# https://leetcode.com/problems/subsets/

# category - combinations/permutations/subsets
# strategy - recursion, backtracking

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # initial solution
        # time/space... extra space needed for dupes
        dupes = set()
        sets = [[]]

        def recur(subset):
            if not subset:
                return

            dupes.add(tuple(subset))
            sets.append(subset)

            for i in range(len(subset)):
                s = subset[:i] + subset[i+1:]
                if tuple(s) not in dupes:
                    recur(s)

        recur(nums)
        return sets

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # simplified recursive
        # O(n2^n) time, O(n^2) space
        sets = [[]]

        for num in nums:
            sets += [s + [num] for s in sets]

        return sets

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        # recursive backtracking
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # similar here to array permutations problem
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()

        return output

    def subsets4(self, nums: List[int]) -> List[List[int]]:
        # use bit masks to generate sets
        # first generate all possible bit masks
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output


s = Solution()
# s.subsets2([1, 2, 3, 4, 5, 6, 7, 8, 10, 0])
# assert s.subsets2([1, 2, 3]) == [
#     [],
#     [3],
#     [1],
#     [2],
#     [1, 2, 3],
#     [1, 3],
#     [2, 3],
#     [1, 2],
# ]
