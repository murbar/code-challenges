# https://leetcode.com/problems/container-with-most-water/

# dynamic programming?
# two pointers?


class Solution:
    def maxArea(self, heights) -> int:
        # brute force, O(n^2) time
        max_area = 0

        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                max_area = max(max_area, height * width)

        return max_area

    def maxArea2(self, heights) -> int:
        # linear time
        # two pointers, one at each end
        # move the shortest one in until they meet
        # check max area at each iteration
        max_area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            max_area = max(max_area, height * width)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area


s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
