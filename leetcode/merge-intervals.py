# https://leetcode.com/problems/merge-intervals/

# if start of one interval is equal to or less than end of another, merge them
# merged is the start of the first, and the end of the second
# probably necessary to sort the input

# could be done as a graph traversal where each node is connected to nodes it overlaps with
# then visit all graph components and record lowest start and highest end
# but this is inefficient at O(n^2) time

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort, then walk through the list
        # O(n lg n) time
        # O(n) space if we allocate a new sorted list, O(1) if we sort in place

        if not len(intervals):
            return []

        # intervals.sort() to sort in place and conserve memory
        intervals = sorted(intervals, key=lambda i: i[0])
        start = intervals[0][0]
        end = intervals[0][1]
        merged = []

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= end:
                end = max(end, e)
            else:
                merged.append([start, end])
                start = s
                end = e

        merged.append([start, end])
        return merged

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        # slightly simplified version of the algorithm above
        intervals.sort(key=lambda i: i[0])
        merged = []

        for interval in intervals:
            last = merged[-1] if merged else None
            # this is the first interval we've seen or it does not overlap with the last one
            if not last or last[1] < interval[0]:
                merged.append(interval)
            else:
                # it overlaps, merge the current with the last
                last[1] = max(last[1], interval[1])

        return merged


s = Solution()

assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert s.merge([[1, 4], [2, 3]]) == [[1, 4]]
assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
    [1, 6], [8, 10], [15, 18]]
assert s.merge([[1, 3], [2, 6], [6, 10], [15, 18]]) == [[1, 10], [15, 18]]

assert s.merge2([[1, 4], [4, 5]]) == [[1, 5]]
assert s.merge2([[1, 4], [2, 3]]) == [[1, 4]]
assert s.merge2([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
    [1, 6], [8, 10], [15, 18]]
assert s.merge2([[1, 3], [2, 6], [6, 10], [15, 18]]) == [[1, 10], [15, 18]]
