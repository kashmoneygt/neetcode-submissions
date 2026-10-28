class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # use cost as DP array and set DP[-1] = 0

        # cost looks like [10, 15, 20, 0]
        # we know last 2 (n and n-1) won't change, so we start at n-2 (len-3)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
