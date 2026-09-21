class MyStack:

    def __init__(self):
        self.st = collections.deque()

    def push(self, x: int) -> None:
        self.st.append(x)
    
        for i in range(len(self.st) - 1):
            self.st.append(self.st.popleft())

    def pop(self) -> int:
        return self.st.popleft()

    def top(self) -> int:
        return self.st[0]

    def empty(self) -> bool:
        return not self.st


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()