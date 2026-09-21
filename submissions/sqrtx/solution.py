class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        i, j = 0, x // 2
        while i < j:
            mid = (i + j + 1) // 2
            prod = mid * mid
            if prod == x:
                return mid
            elif prod < x:
                i = mid
            elif prod > x:
                j = mid - 1
        
        return i
