class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minP, maxP = 1, 1
        res = nums[0]

        for num in nums:
            tmp = minP * num
            minP = min(num, minP * num, maxP * num)
            maxP = max(num, maxP * num, tmp)
            res = max(res, maxP)
        
        return res
