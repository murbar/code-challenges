# https://leetcode.com/problems/gas-station/

# a circuit can only be completed if the sum of gas is >= the sum of costs
# if A cannot reach C in the sequence A -> B -> C, then B cannot either


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        in_tank = 0
        total_gas = 0
        location = 0

        for i in range(len(gas)):
            net_cost = gas[i] - cost[i]
            in_tank += net_cost
            total_gas += net_cost

            if in_tank < 0:
                location = i + 1
                in_tank = 0

        # if total gas is negative after visiting every station, there is no way to make a circuit
        return location if total_gas >= 0 else -1


s = Solution()
assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
