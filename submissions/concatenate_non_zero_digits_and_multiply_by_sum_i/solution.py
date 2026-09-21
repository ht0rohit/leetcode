class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        summ, mul = 0, 1
        while n != 0:
            digit = n % 10
            if digit != 0:
                x += digit * mul
                summ += digit
                mul *= 10
            n //= 10

        return x * summ