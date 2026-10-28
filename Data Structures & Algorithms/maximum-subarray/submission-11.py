class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        res = nums[0]

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum = max(cur_sum + num, num)
            res = max(res, cur_sum)
        
        return res