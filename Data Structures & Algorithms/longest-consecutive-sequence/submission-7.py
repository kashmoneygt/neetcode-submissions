class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        res = 0
        for num in nums:
            if num - 1 not in seen:
                streak = 0
                while num + streak in seen: streak += 1
                res = max(res, streak)
        
        return res
        