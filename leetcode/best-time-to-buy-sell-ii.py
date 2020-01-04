# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

'''
we need to locate all pairs of local low and highs on the price graph
return the total of their differences
or, more simply, just accumulate profit for each profitable day (price is greater than day before)
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        low, high = prices[0], prices[0]
        profit = 0

        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            low = prices[i]

            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]

            profit += high - low

        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        # simplify the code by incrementing the profit as the prices increase
        # while we crawl over the graph
        # preferred solution
        if len(prices) < 2:
            return 0

        profit = 0
        last_price = prices[0]

        for p in prices:
            if p > last_price:
                profit += p - last_price

            last_price = p

        return profit


s = Solution()
assert s.maxProfit([5]) == 0
assert s.maxProfit([1, 2]) == 1
assert s.maxProfit([5, 2]) == 0
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert s.maxProfit([1, 2, 3, 4, 5]) == 4

assert s.maxProfit2([5]) == 0
assert s.maxProfit2([1, 2]) == 1
assert s.maxProfit2([5, 2]) == 0
assert s.maxProfit2([7, 1, 5, 3, 6, 4]) == 7
assert s.maxProfit2([1, 2, 3, 4, 5]) == 4
