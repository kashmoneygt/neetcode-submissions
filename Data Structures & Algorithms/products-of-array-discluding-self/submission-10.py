class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force - n^2 / 1
        # division => n / 1
        # prefix and suffix - n / n
        # prefix and suffix optimal - n / 1
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        