class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)

        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        sCase1 = 1
        sCase2 = 2

        for i in range(2, n):
            res = sCase1 + sCase2
            sCase1 = sCase2
            sCase2 = res

        return res
