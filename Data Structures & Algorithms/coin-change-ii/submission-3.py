class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1 # 1 way to get to amount = 0 (no coins)


        for c in coins[::-1]:
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a] # looking below
                if a - c >= 0:
                    nextDP[a] += nextDP[a - c] # looking right

            dp = nextDP

        return dp[amount]
