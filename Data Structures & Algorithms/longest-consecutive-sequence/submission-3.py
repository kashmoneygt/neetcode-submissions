class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        
        numSet = set(nums)
        for num in nums:
            if num - 1 not in numSet:
                streak = 0
                while num + streak in numSet:
                    streak += 1

                res = max(res, streak)

        return res
