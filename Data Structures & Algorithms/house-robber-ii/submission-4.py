class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helper(nums[:-1]), self.helper(nums[1:]), nums[0])

    def helper(self, nums):
        one, two = 0, 0

        for i in range(len(nums)):
            temp = max(nums[i] + one, two)
            one = two
            two = temp
            
        return two