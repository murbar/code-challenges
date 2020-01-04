# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# return a set intersection for two array BUT result elements should appear
# as many times as they appear in both lists
# instead of using a plain set, use a dictionary to keep track of counts of items


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []

        # add all items in nums1 to dictionary
        for n in nums1:
            seen[n] = seen.get(n, 0) + 1

        # bail early if no items in nums1, no intersection
        if not seen:
            return result

        # check if items in nums two are in the dictionary and have count > 0
        # if found, decrement count and add item to result array
        for n in nums2:
            if seen.get(n, 0) != 0:
                result.append(n)
                seen[n] = seen[n] - 1

        return result
