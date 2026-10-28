class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy()
            for t in dp:
                nextDP.add(nums[i] + t) # add nums[i] to every target

            dp = nextDP

        return target in dp
