class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            diff = val - self.min
            self.stack.append(diff)
            self.min = min(self.min, val)
    
    def pop(self) -> None:
        if not self.stack:
            return
        diff = self.stack.pop()
        if diff < 0:
            self.min -= diff
        
    def top(self) -> int:
        diff = self.stack[-1]
        if diff > 0:
            return diff + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
