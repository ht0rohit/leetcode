class Solution:
    def getSumOfKthPowerOfDigits(self, n: int, k: int) -> int:
        result = 0

        while n != 0:
            result += (n % 10) ** k
            n //= 10

        return result

    def isArmstrong(self, n: int) -> bool:
        length = 0
        tempN = n

        while tempN:
            length += 1
            tempN //= 10

        return self.getSumOfKthPowerOfDigits(n, length) == n