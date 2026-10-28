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

            if val < self.min: self.min = val

    def pop(self) -> None:
        if not self.stack: return

        val = self.stack.pop()
        if val < 0: self.min -= val

    def top(self) -> int:
        val = self.stack[-1]
        if val > 0: return val + self.min
        return self.min
        

    def getMin(self) -> int:
        return self.min
