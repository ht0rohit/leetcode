class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = False
        while n:
            n &= (n - 1)
            res = not res
            if not res:
                return False
            
            
        return True