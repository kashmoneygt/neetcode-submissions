class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically increasing stack - n / n
        # dp from back - n / 1
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            
            stack.append((t, i))
        
        return res