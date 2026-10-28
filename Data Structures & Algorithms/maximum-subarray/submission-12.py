class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        res = nums[0]

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            res = max(res, cur_sum)
        
        return res