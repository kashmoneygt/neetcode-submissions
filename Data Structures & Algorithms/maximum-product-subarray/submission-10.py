class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            temp = curMax * num
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, num * curMin, temp)
            res = max(res, curMax)
        
        return res