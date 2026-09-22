class StockSpanner:

    def __init__(self):
        self.stock = [10^5 + 1]

    def next(self, price: int) -> int:
        self.stock.append(price)
        i, span = len(self.stock) - 1, 0
        while i > 0:
            if self.stock[i] <= price:
                span += 1
                i -= 1
            else:
                return span

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)