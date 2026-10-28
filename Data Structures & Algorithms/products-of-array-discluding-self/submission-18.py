class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        mult = nums[0]
        for i in range(1, len(nums)):
            res[i] *= mult
            mult *= nums[i]
        
        print(res)

        mult = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= mult
            mult *= nums[i]
        
        return res

