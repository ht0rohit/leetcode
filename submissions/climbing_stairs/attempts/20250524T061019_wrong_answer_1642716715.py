class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0]*(n+1)
        if n==1:
            ways[n] = 1
            return ways[n]
        for i in range(2, n+1):
            ways[i] = self.climbStairs(i-1) + 1

        return ways[n]
