# https://leetcode.com/problems/house-robber/

# maximize take without robbing two adjacent houses
# first thought is to take the max of robbing every other house
# starting at the first house and then starting at the second house
# but we want to take the max of robbing current house, or the last and the next

# no houses is 0, one house is the the value of the house,
# two houses is the max of either house
# with three houses it gets interesting...
# dynamic programming... "bottom up processing"
# https://www.youtube.com/watch?v=xlvhyfcoQa4

from typing import List


class Solution:
    def rob(self, houses: List[int]) -> int:
        if not houses:
            return 0

        if len(houses) == 1:
            return houses[0]

        # 2 or more houses?
        # array to hold our maximum amount of money at each house
        n_houses = len(houses)
        max_hauls = [houses[0]] * n_houses
        max_hauls[1] = max(houses[0], houses[1])
        # start at third house, first two are already set
        for i in range(2, n_houses):
            # taking this house and last house will trigger alarm
            this_house_and_1_house_down = houses[i] + max_hauls[i-2]
            last_house = max_hauls[i-1]
            max_hauls[i] = max(this_house_and_1_house_down, last_house)

        return max_hauls[-1]


s = Solution()
assert s.rob([]) == 0
assert s.rob([4]) == 4
assert s.rob([1, 3]) == 3
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 7, 9, 3, 1]) == 12
