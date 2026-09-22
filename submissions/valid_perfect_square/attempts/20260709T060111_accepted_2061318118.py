class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 0, num
        while i <= j:
            mid = (i + j) // 2
            prod = mid * mid
            if prod == num:
                return True
            elif prod < num:
                i = mid + 1
            elif prod > num:
                j = mid - 1
        
        return False