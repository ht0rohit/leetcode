class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lis = [amount+1] * (amount + 1)
        lis[0] = 0
        for elem in range(1, amount + 1):
            for c in coins:
                if elem - c >= 0:
                    lis[elem] = min(lis[elem], 1 + lis[elem - c])

        return lis[amount] if lis[amount] != amount + 1 else -1