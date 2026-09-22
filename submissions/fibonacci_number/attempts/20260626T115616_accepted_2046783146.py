class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        temp = -1
        for i in range(2, n + 1):
            c = a + b
            temp = b
            b = c
            a = temp

        return c