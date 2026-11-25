class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = { 0 : 1 }

        res, curSum = 0, 0
        for i, num in enumerate(nums):
            curSum += num
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        
        return res