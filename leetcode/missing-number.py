# https://leetcode.com/problems/missing-number/

# can be done with bit manipulation too, using XOR


class Solution:
    def missingNumber(self, nums) -> int:
        # efficient solution relies on rule for sum of numbers 1 to n:
        #   n*(n+1)/2
        # this list includes 0, so n for a complete list would be len(nums) - 1
        # but we're missing a value so len(nums) is correct
        n = len(nums)
        target = n * (n + 1) // 2
        actual = sum(nums)
        return target - actual

    def missingNumber2(self, nums) -> int:
        # if we didn't know the formula for sum of numbers 1 to n
        # we can add all nums to a set then iterate over range(n)
        # and check for each number
        # less efficient but works fine
        num_set = set(nums)
        n = len(nums) + 1
        for num in range(n):
            if num not in num_set:
                return num


s = Solution()
assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert s.missingNumber([3, 0, 1]) == 2
assert s.missingNumber([1]) == 0
assert s.missingNumber([0]) == 1
assert s.missingNumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert s.missingNumber2([3, 0, 1]) == 2
assert s.missingNumber2([1]) == 0
assert s.missingNumber2([0]) == 1
