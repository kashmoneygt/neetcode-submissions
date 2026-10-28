class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []
        for pos, sp in cars:
            stack.append((target - pos) / sp)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)