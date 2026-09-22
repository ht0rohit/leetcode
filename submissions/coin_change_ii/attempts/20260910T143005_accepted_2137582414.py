class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def fun(i, rem):
            if rem == 0:
                return 1
            
            if rem < 0 or i >= len(coins):
                return 0

            ways = 0
            ways += fun(i, rem - coins[i])
            ways += fun(i + 1, rem)

            return ways


        return fun(0, amount)