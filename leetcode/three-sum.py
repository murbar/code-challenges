# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # pointers i, j, k for values a, b, c
        # first, sort the values in ascending order
        # this solution relies on a sorted input for a efficient solution
        # O(n^2) time, best case for this problem?
        nums = sorted(nums)
        triplets = []
        target = 0

        # check each element as a, up to second-from-last
        for i in range(len(nums) - 2):
            a = nums[i]

            # this value is that same as last iteration, skip to next
            if i > 0 and a == nums[i-1]:
                continue

            # if a is larger than target in sorted list, all following elements are also larger
            if a > target:
                break

            # set j to next element, k to last
            j = i + 1
            k = len(nums) - 1

            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c == target:
                    triplets.append([a, b, c])
                    # move j and k to next value different from current values
                    # keep moving while values are unchanged
                    while j < k and b == nums[j+1]:
                        j += 1
                    while j < k and c == nums[k-1]:
                        k -= 1
                    # next values are different
                    j += 1
                    k -= 1
                # k is the largest value (end of sorted list) so move it down if overshooting target
                elif a + b + c > target:
                    k -= 1
                # less than target, move j to next largest value
                else:
                    j += 1

        return triplets


s = Solution()
assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
assert s.threeSum([-1, 0, 1]) == [[-1, 0, 1]]
assert s.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
