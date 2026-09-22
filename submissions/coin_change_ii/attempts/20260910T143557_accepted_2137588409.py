class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        
        def fun(i, rem):
            if rem == 0:
                return 1
            
            if rem < 0 or i == len(coins):
                return 0

            if dp[i][rem] != -1:
                return dp[i][rem]

            dp[i][rem] = fun(i, rem - coins[i]) + fun(i + 1, rem)

            return dp[i][rem]


        return fun(0, amount)