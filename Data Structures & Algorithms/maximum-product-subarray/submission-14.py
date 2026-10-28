class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minP, maxP = 1, 1

        for num in nums:
            temp = minP
            minP = min(num * maxP, num * minP, num)
            maxP = max(num * maxP, num * temp, num)
            res = max(res, minP, maxP)
        
        return res
