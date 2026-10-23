class MinStack:

    def __init__(self):
        self.stack = []
        self.sMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.sMin) == 0:
            self.sMin.append(val)
        elif val < self.sMin[-1]:
            self.sMin.append(val)
        else:
            self.sMin.append(self.sMin[-1])

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.sMin.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.sMin[-1]
