class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores (i, temp)
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                old_i, _ = stack.pop()
                res[old_i] = i - old_i
            
            stack.append((i, temp))

        return res