class MinStack:

    def __init__(self):
        self.st = []
        self.min = None

    def push(self, value: int) -> None:
        if not self.min or value < self.min:
            self.min = value
        self.st.append((value, self.min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()