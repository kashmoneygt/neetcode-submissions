class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                old_i, old_temp = stack.pop()
                res[old_i] = i - old_i
            
            stack.append((i, temp))

        return res