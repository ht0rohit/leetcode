class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        
        elem = s
        maxel = s
        for i in range(2, n + 1):
            if i % 2 == 0:
                elem += m
            else:
                elem -= 1
            maxel = max(maxel, elem)
            
        return maxel