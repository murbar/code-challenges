# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


def maxProfit(prices) -> int:
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = prices[1] - min_price

    for i in range(1, len(prices)):
        current_price = prices[i]
        potential_profit = current_price - min_price
        max_profit = max(potential_profit, max_profit)
        min_price = min(current_price, min_price)

    # no transaction if profit is negative
    return max(max_profit, 0)


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
assert maxProfit([]) == 0
assert maxProfit([5]) == 0
