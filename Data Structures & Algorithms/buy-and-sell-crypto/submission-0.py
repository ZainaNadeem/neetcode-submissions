class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        
        for price in prices:
            # Update minimum price seen so far
            minPrice = min(minPrice, price)
            
            # Calculate profit if we sell at current price
            profit = price - minPrice
            
            # Update maximum profit
            maxProfit = max(maxProfit, profit)
        
        return maxProfit