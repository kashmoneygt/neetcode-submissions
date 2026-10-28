class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        mult = 1
        for i in range(len(nums)):
            res[i] = mult
            mult *= nums[i]
        
        mult = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= mult
            mult *= nums[i]
        
        return res