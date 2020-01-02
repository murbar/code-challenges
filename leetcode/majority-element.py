# https://leetcode.com/problems/majority-element/

# first instinct is to use a hash table to store counts
# if we find an element with count > n/2, return it
# input is non-empty array, majority always exists
# O(n) time and space
# Boyer-Moore is a neat trick to reduce space complexity to O(1)
#   only works if majority element exists


class Solution:
    def majorityElement(self, nums) -> int:
        counts = {}
        # strictly more than n/2
        majority = (len(nums) // 2) + 1
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] == majority:
                return n

        return None

    # Boyer-Moore Voting Algorithm
    def majorityElement2(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
