class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force - nested for - n^2 / 1
        # two pointers (l and r) - n / 1
        # DP - track maxProf and minBuy - n / 1
        res = 0
        minSoFar = prices[0]

        for price in prices[1:]:
            if price < minSoFar:
                minSoFar = price
            else:
                res = max(res, price - minSoFar)

        return res