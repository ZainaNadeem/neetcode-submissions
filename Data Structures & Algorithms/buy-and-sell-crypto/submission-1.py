from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = inf
        profit = 0
        for i in prices:
            curr_price = i - min_price
            min_price = min(i, min_price)
            if curr_price > profit:
                profit = curr_price
        return profit