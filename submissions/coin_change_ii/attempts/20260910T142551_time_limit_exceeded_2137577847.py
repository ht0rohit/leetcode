class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def fun(i, rem):
            if rem == 0:
                return 1
            elif rem < 0:
                return 0

            ways = 0
            for c in range(i, len(coins)):
                ways += fun(c, rem - coins[c])

            return ways


        return fun(0, amount)