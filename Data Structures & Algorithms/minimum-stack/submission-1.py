class MinStack:
    # stack holding (val, min) tuples or two stacks - 1 / n
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append((val, val))
        else:
            self.s.append((val, min(val, self.s[-1][1])))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
