class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            if total < 0:    # if our curr diff makes total neg,
                total = 0    # reset total and set res (start) to next index
                res = i + 1  # if next index also sucks, it won't update res (start)

        return res