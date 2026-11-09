class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # store indices
        maxArea = 0
        n = len(heights)

        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, width * height)
            
            stack.append(i)
        
        return maxArea