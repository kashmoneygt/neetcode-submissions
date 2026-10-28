class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minP, maxP = 1, 1
        res = max(nums)

        for num in nums:
            oldMinP = minP

            minP = min(minP * num, maxP * num, num)
            
            maxP = max(maxP * num, oldMinP * num, num)
            
            res = max(res, minP, maxP)

        return res

