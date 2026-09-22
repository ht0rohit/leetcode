class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        i, j = 0, x
        while i <= j:
            mid = (i + j) // 2
            prod = mid * mid
            if prod == x:
                return mid
            elif prod < x:
                i = mid + 1
            elif prod > x:
                j = mid - 1
        
        if prod < x:
            return mid
        else:
            return mid - 1