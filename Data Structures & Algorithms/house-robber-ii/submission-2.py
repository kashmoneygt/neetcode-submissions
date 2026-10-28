class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            nums[0], # incase there's only 1 house
            self.helper(nums[:-1]),
            self.helper(nums[1:])
        )

    def helper(self, nums) -> int:
        rob1 = 0 # i-2
        rob2 = 0 # i-1

        for n in nums:
            newRob = max(n + rob1, rob2)
            rob1 = rob2   # now becomes i-1
            rob2 = newRob # now becomes i

        return rob2
