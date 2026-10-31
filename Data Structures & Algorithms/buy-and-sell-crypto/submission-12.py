class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float("inf"), 0
        for i, price in enumerate(prices):
            maxProfit = max(maxProfit, price - minPrice)
            if price < minPrice:
                minPrice = price
        
        return maxProfit