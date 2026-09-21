class Solution:
    def integerBreak(self, n: int) -> int:
        maxProd = 0
        for k in range(2, n+1):
            num = n // k
            rem = n % k
            if rem == 0:
                prod = int(math.pow(num, k))
            else:
                prod = int(math.pow(num, k - rem)) * int(math.pow(num + 1, rem))
            if prod > maxProd:
                maxProd = prod

        return maxProd