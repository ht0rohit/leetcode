class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, math.ceil(math.sqrt(c))
        while i <= j:
            sq = math.pow(i, 2) + math.pow(j, 2)
            if sq == c:
                return True
            elif sq > c:
                j -= 1
            else:
                i += 1

        return False