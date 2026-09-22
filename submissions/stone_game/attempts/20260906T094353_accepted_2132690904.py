class Solution:
    def stoneGame(self, piles):
        n = len(piles)

        memo = [[None] * n for _ in range(n)]

        def dp(l, r):
            if l == r:
                return piles[l]

            if memo[l][r] is not None:
                return memo[l][r]

            take_left = piles[l] - dp(l + 1, r)
            take_right = piles[r] - dp(l, r - 1)

            memo[l][r] = max(take_left, take_right)

            return memo[l][r]

        return dp(0, n - 1) > 0