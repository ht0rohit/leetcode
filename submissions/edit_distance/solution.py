class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return m or n

        dp = [0] * (n + 1)
        for j in range(1, n + 1):
            dp[j] = j

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                temp = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(prev, dp[j], dp[j - 1]) + 1

                prev = temp


        return dp[-1]