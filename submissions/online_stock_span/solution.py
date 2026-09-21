class StockSpanner:

    def __init__(self):
        self.st = []
        self.count = 0

    def next(self, price: int) -> int:
        self.count = 1
        if not self.st:
            self.st.append((price, self.count))
            print(self.st)
            return self.count
        while self.st and price >= self.st[-1][0]:
            self.count += self.st[-1][1]
            self.st.pop()
        self.st.append((price, self.count))
        print(self.st)
        return self.count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)