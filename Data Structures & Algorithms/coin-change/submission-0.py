class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # 0 to amount, start with max value for each
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # in our example:
                    # coin = 4 and a = 7
                    # dp[7] = 1 + dp[3]
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != (amount + 1) else -1
