class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force - nested for loops - n^2 / 1
        # sorting - nlogn / 1
        # hashset - n / n
        # hashset length - n / n
        seen = set()
        for num in nums:
            if num in seen: return True
            seen.add(num)
        
        return False
