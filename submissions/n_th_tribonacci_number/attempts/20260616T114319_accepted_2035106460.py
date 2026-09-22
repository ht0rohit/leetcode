class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        trib = [0, 1, 1] + [-1] * (n-2)
        for i in range(3, n+1):
            trib[i] = trib[i-1] + trib[i-2] + trib[i-3]

        return trib[-1]