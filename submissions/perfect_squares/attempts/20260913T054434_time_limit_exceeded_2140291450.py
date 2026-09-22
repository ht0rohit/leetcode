class Solution:
    def numSquares(self, n: int) -> int:
        safe = int(math.sqrt(n))
        dp = [[0] * (n + 1) for _ in range(safe + 1)]


        def backt(m, sq):
            if sq == n:
                return 0
            
            if sq > n or m > safe:
                return float('inf')

            if dp[m][sq] != 0:
                return dp[m][sq]

            dp[m][sq] = min(backt(m + 1, sq), 1 + backt(m, sq + m * m))
            return dp[m][sq]


        return backt(1, 0)