class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        
        res = 0
        for num in nums:
            if (num - 1) not in seen:
                seq = 1
                while num + seq in seen:
                    seq += 1
                
                res = max(res, seq)
        
        return res