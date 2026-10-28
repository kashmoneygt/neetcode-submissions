class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(houses):
            rob1, rob2 = 0, 0
            for num in houses:
                curI = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = curI
            return rob2
        
        return max(
            helper(nums[1:]),
            helper(nums[:-1]),
            nums[0]
        )