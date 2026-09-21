class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(x, n):
            result = 1

            while n:
                if n & 1:
                    result = result * x % MOD

                x = x * x % MOD
                n >>= 1

            return result

        even = (n + 1) // 2
        odd = n // 2

        return power(5, even) * power(4, odd) % MOD