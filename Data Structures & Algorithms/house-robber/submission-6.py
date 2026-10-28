class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one, two = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(nums[i] + one, two)
            one = two
            two = temp
            
        return two