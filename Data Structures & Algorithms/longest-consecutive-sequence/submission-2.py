class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force (not checking start of seq) - n^2 / n
        # sorting - nlogn / 1
        # hashset - n / n
        # hashmap - n / n
        seen = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in seen:
                i = 1
                while num + i in seen:
                    i += 1
                res = max(res, i)

        return res
