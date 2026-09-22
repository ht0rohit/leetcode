class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        step1, step2 = 1, 2
        for i in range(2, n):
            step = step1 + step2
            step1 = step2
            step2 = step

        return step