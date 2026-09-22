class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_up = []
        for coin in coins:
            if coin <= amount:
                coins_up += [coin]
            else:
                break

        num_coins = [-1] * (amount) + [0]
        
        if amount == 0:
            return 0
        elif amount > 0:
            if 1 in coins_up:
                num_coins[0] = 1
        
        for i in range(1, amount):
            minn = []
            for j in range(len(coins_up)):
                if i-coins_up[j] >= -1 and num_coins[i-coins_up[j]] != -1:
                    minn += [num_coins[i-coins_up[j]] + 1]
                
            if minn:
                num_coins[i] = min(minn)
            else:
                num_coins[i] = -1

        return num_coins[-2]