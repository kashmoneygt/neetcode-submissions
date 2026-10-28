class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minSoFar = prices[0]

        for price in prices[1:]:
            if price < minSoFar:
                minSoFar = price
            else:
                res = max(res, price - minSoFar)

        return res