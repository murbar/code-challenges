# https://leetcode.com/problems/contains-duplicate/solution/

# might also sort the list and check if any two adjacent elements are the same
# O(n log n) time, constant space


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O(n) time and space
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        # very slightly more efficient if duplicate occurs early in the list
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
