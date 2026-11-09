class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        for p, s in pairs: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)