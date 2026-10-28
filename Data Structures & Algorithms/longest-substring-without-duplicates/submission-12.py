class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force - for i and j - nm / m
        # sliding window - n / m (total # of unique chars)

        l = 0
        res = 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            res = max(res, r - l + 1)
        
        return res
