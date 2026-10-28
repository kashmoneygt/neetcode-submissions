class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force - n^2 / 1
        # sorting - nlogn / n
        # hashmap 2pass - n / n
        # hashmap 1pass - n / n
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: return [seen[diff], i]
            seen[num] = i
        
        return [-1, -1]
