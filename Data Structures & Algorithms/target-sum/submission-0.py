class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int) # represents dp for i = 0 (using 0 items)

        dp[0] = 1 # 1 way to sum to 0 using 0 items

        for i in range(len(nums)):
            nextDP = defaultdict(int)
            for cur_sum, count in dp.items():
                nextDP[cur_sum + nums[i]] += count
                nextDP[cur_sum - nums[i]] += count
            
            dp = nextDP

        return dp[target]