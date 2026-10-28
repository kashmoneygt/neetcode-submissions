class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force - n^2 / 1
        # two pointer - n / 1
        res = 0
        
        l, r = 0, len(heights) - 1
        while l < r:
            res = max(
                res,
                min(heights[l], heights[r]) * (r - l)
            )
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
