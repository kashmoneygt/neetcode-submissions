class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if (i, buying) in dp:
                return dp[(i, buying)]
            if i >= len(prices):
                return 0
            
            if buying:
                dp[(i, buying)] = max(
                    dfs(i + 1, not buying) - prices[i],
                    dfs(i + 1, buying)
                )
            else:
                dp[(i, buying)] = max(
                    dfs(i + 2, not buying) + prices[i],
                    dfs(i + 1, buying)
                )
            
            return dp[(i, buying)]
        
        return dfs(0, True)