class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If buy -> move index to i + 1
        # If sell -> move index to i + 2 (cooldown)

        dp = {} # (i, buying bool) -> max profit

        def dfs(i, buying) -> int:
            if i >= len(prices):
                return 0 # empty arr -> no profit
            if (i, buying) in dp:
                return dp[(i, buying)] # caching
            
            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
